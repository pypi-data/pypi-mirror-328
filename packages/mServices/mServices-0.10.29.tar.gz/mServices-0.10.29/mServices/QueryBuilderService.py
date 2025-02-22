from django.db import connection
from datetime import datetime

class QueryBuilderService:
    def __init__(self, table):
        self.table = table
        self.select_columns = '*'
        self.conditions = []
        self.or_conditions = []
        self.order_by = ''
        self.limit = None
        self.offset = None
        self.group_by = ''

    def select(self, *columns):
        """Select specific columns for the query."""
        self.select_columns = ', '.join(columns) if columns else '*'
        return self

    def where(self, column, value, operator="="):
        """Apply a WHERE condition."""
        self.conditions.append((f"{column} {operator} %s", [value]))
        return self

    def orWhere(self, column, value, operator="="):
        """Apply an OR WHERE condition."""
        self.or_conditions.append((f"{column} {operator} %s", [value]))
        return self

    def whereIn(self, column, values):
        """Filter results where column value is in a list."""
        placeholders = ', '.join(['%s'] * len(values))
        self.conditions.append((f"{column} IN ({placeholders})", values))
        return self

    def whereNotIn(self, column, values):
        """Filter results where column value is not in a list."""
        placeholders = ', '.join(['%s'] * len(values))
        self.conditions.append((f"{column} NOT IN ({placeholders})", values))
        return self

    def whereBetween(self, column, start, end):
        """Filter results where column value is between two values."""
        self.conditions.append((f"{column} BETWEEN %s AND %s", [start, end]))
        return self

    def whereDate(self, column, date_value):
        """Filter results by exact date."""
        self.conditions.append((f"DATE({column}) = %s", [date_value]))
        return self

    def whereMonth(self, column, month):
        """Filter results by month."""
        self.conditions.append((f"MONTH({column}) = %s", [month]))
        return self

    def whereDay(self, column, day):
        """Filter results by day of the month."""
        self.conditions.append((f"DAY({column}) = %s", [day]))
        return self

    def whereYear(self, column, year):
        """Filter results by year."""
        self.conditions.append((f"YEAR({column}) = %s", [year]))
        return self

    def whereTime(self, column, time_value):
        """Filter results by time."""
        self.conditions.append((f"TIME({column}) = %s", [time_value]))
        return self

    def whereNull(self, column):
        """Filter records where column is NULL."""
        self.conditions.append((f"{column} IS NULL", []))
        return self

    def whereNotNull(self, column):
        """Filter records where column is NOT NULL."""
        self.conditions.append((f"{column} IS NOT NULL", []))
        return self

    def wherePast(self, column):
        """Filter results where date column is in the past."""
        self.conditions.append((f"{column} < %s", [datetime.now()]))
        return self

    def whereFuture(self, column):
        """Filter results where date column is in the future."""
        self.conditions.append((f"{column} > %s", [datetime.now()]))
        return self

    def whereNowOrPast(self, column):
        """Filter results where date column is now or in the past."""
        self.conditions.append((f"{column} <= %s", [datetime.now()]))
        return self

    def whereNowOrFuture(self, column):
        """Filter results where date column is now or in the future."""
        self.conditions.append((f"{column} >= %s", [datetime.now()]))
        return self

    def whereToday(self, column):
        """Filter results where date column is today."""
        today = datetime.now().date()
        self.conditions.append((f"DATE({column}) = %s", [today]))
        return self

    def whereBeforeToday(self, column):
        """Filter results where date column is before today."""
        today = datetime.now().date()
        self.conditions.append((f"DATE({column}) < %s", [today]))
        return self

    def whereAfterToday(self, column):
        """Filter results where date column is after today."""
        today = datetime.now().date()
        self.conditions.append((f"DATE({column}) > %s", [today]))
        return self

    def orderBy(self, column, direction="asc"):
        """Apply ORDER BY sorting."""
        self.order_by = f"ORDER BY {column} {direction.upper()}"
        return self

    def groupBy(self, *columns):
        """Group results by specified columns."""
        self.group_by = f"GROUP BY {', '.join(columns)}"
        return self

    def count(self):
        """Get the count of records."""
        return self.aggregate("COUNT(*)")

    def max(self, column):
        """Get the max value of a column."""
        return self.aggregate(f"MAX({column})")

    def min(self, column):
        """Get the min value of a column."""
        return self.aggregate(f"MIN({column})")

    def avg(self, column):
        """Get the average value of a column."""
        return self.aggregate(f"AVG({column})")

    def pluck(self, column):
        """Get a list of values for a single column."""
        query, values = self.build_query(select_column=column)
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            return [row[0] for row in cursor.fetchall()]

    def aggregate(self, agg_function):
        """Helper method to execute an aggregate function."""
        query, values = self.build_query(select_column=agg_function)
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            return cursor.fetchone()[0]

    def build_query(self, select_column=None):
        """Construct the SQL query dynamically."""
        query = f"SELECT {select_column or self.select_columns} FROM {self.table}"
        values = []
        
        if self.conditions:
            query += " WHERE " + " AND ".join([cond[0] for cond in self.conditions])
            values.extend([val for cond in self.conditions for val in cond[1]])

        if self.or_conditions:
            query += " OR " + " OR ".join([cond[0] for cond in self.or_conditions])
            values.extend([val for cond in self.or_conditions for val in cond[1]])

        if self.group_by:
            query += f" {self.group_by}"

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
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def paginate(self, page=1, per_page=10):
        """Paginate the query results."""
        self.limit = per_page
        self.offset = (page - 1) * per_page
        return self.execute()
