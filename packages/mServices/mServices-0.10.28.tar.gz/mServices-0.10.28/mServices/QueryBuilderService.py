from django.db import connection

class QueryBuilderService:
    def __init__(self, table):
        self.table = table
        self.select_columns = '*'
        self.conditions = []
        self.order_by = ''
        self.limit = None
        self.offset = None

    def select(self, *columns):
        """Select specific columns for the query."""
        self.select_columns = ', '.join(columns) if columns else '*'
        return self

    def where(self, column, value, operator="="):
        """Apply a WHERE condition."""
        self.conditions.append((f"{column} {operator} %s", value))
        return self

    def whereLike(self, columns, search_string):
        """Apply a LIKE condition for multiple columns (search functionality)."""
        like_conditions = [f"{col} LIKE %s" for col in columns]
        self.conditions.append((f"({' OR '.join(like_conditions)})", [f"%{search_string}%"] * len(columns)))
        return self

    def orderBy(self, column, direction="asc"):
        """Apply ORDER BY sorting."""
        self.order_by = f"ORDER BY {column} {direction.upper()}"
        return self

    def apply_conditions(self, filter_json, allowed_filters, search_string, search_columns):
        """Apply filters and search conditions in one method."""
        # Apply filters from JSON
        for key, value in filter_json.items():
            if key in allowed_filters:
                self.where(key, value)

        # Apply search if a search string is provided
        if search_string:
            self.whereLike(search_columns, search_string)
        
        return self

    def paginate(self, page=1, per_page=10):
        """Paginate the query results."""
        self.limit = per_page
        self.offset = (page - 1) * per_page
        return self.execute()

    def build_query(self):
        """Construct the SQL query dynamically."""
        query = f"SELECT {self.select_columns} FROM {self.table}"
        values = []
        if self.conditions:
            query += " WHERE " + " AND ".join([cond[0] for cond in self.conditions])
            for cond in self.conditions:
                if isinstance(cond[1], list):
                    values.extend(cond[1])
                else:
                    values.append(cond[1])
        if self.order_by:
            query += f" {self.order_by}"
        if self.limit is not None:
            query += f" LIMIT {self.limit} OFFSET {self.offset}"
        return query, values

    def execute(self):
        """Execute the built query and return results."""
        query, values = self.build_query()
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return results
