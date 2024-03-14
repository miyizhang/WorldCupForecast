from django.db import connection


def get_recent_matches(home_team, away_team, number_of_matches=5):
    with connection.cursor() as cursor:
        query = '''
        SELECT * FROM matchHistory
        WHERE (home_team = %s AND away_team = %s) OR (home_team = %s AND away_team = %s)
        ORDER BY date DESC
        LIMIT %s
        '''
        cursor.execute(query, [home_team, away_team, away_team, home_team, number_of_matches])
        columns = [col[0] for col in cursor.description]
        recent_matches_list = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return recent_matches_list
