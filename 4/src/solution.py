import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def get_order_sum(connection, month):
    with connection.cursor(cursor_factory=DictCursor) as cursor:
        query = """
            SELECT 
                c.customer_name,
                SUM(o.total_amount) as total_sum
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            WHERE EXTRACT(MONTH FROM o.order_date) = %s
            GROUP BY c.customer_id, c.customer_name
        """
        
        cursor.execute(query, (month,))
        results = cursor.fetchall()
        
        formatted_results = []
        for row in results:
            formatted_results.append(
                f"Покупатель {row['customer_name']} совершил покупок на сумму {int(row['total_sum'])}"
            )
        
        return "\n".join(formatted_results)
# END
