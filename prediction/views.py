from django.shortcuts import render, redirect
from .predictor import predict_match
from .forms import MatchInfoForm
from django.contrib.admin.views.decorators import staff_member_required
import sqlite3
import pandas as pd
from .forms import RegisterForm
from .recentMatch import get_recent_matches

with open("data/country_name.txt", "r", encoding="utf-8") as f:
    info = f.readlines()
    info = list(map(lambda x: x.strip(), info))

English_name = info[:32]
Chinese_name = info[32:]

country_name = {}

for each in zip(English_name, Chinese_name):
    country_name[each[0]] = each[1]


def get_key_from_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return value


# 管理员视图
def admin_home(request):
    conn = sqlite3.connect('./db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM matchInfo", conn)
    # df['match_date'] = pd.to_datetime(df['match_date'], unit='ms').dt.strftime('%Y-%m-%d')
    conn.close()

    data = {'data': df.to_dict(orient='records')}

    return render(request, 'admin/home.html', data)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # 重定向到登录页面
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


@staff_member_required
def update_match_info(request):
    if request.method == 'POST':
        form = MatchInfoForm(request.POST)
        if form.is_valid():
            latest_match_info = form.save()

            # 连接到 SQLite 数据库
            conn = sqlite3.connect('./db.sqlite3')
            cursor = conn.cursor()

            # 插入新的比赛信息
            insert_query = '''INSERT INTO matchInfo (match_date, match_time, team_a, team_b, result)
                              VALUES (?, ?, ?, ?, ?)'''
            data_tuple = (latest_match_info.match_date, latest_match_info.match_time,
                          latest_match_info.team_a, latest_match_info.team_b,
                          latest_match_info.result)
            cursor.execute(insert_query, data_tuple)
            conn.commit()

            # 关闭数据库连接
            cursor.close()
            conn.close()

            return redirect('custom_admin:admin_home')  # 更新成功后的重定向
    else:
        form = MatchInfoForm()

    return render(request, 'admin/update_match_info.html', {'form': form})


@staff_member_required
def edit_match_info(request, match_id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM matchInfo WHERE id = ?", (match_id,))
    match = cursor.fetchone()

    if request.method == 'POST':
        form = MatchInfoForm(request.POST)
        if form.is_valid():
            match_date = form.cleaned_data['match_date']
            match_time = form.cleaned_data['match_time']
            team_a = form.cleaned_data['team_a']
            team_b = form.cleaned_data['team_b']
            result = form.cleaned_data['result']
            cursor.execute(
                "UPDATE matchInfo SET match_date = ?, match_time = ?, team_a = ?, team_b = ? , result = ? WHERE id = ?",
                (match_date,
                 match_time,
                 team_a,
                 team_b,
                 result,
                 match_id))
            conn.commit()
            return redirect('custom_admin:admin_home')
    else:
        form = MatchInfoForm(
            initial={
                'match_date': match[1],
                'match_time': match[2],
                'team_a': match[3],
                'team_b': match[4],
                'result': match[5]})
    conn.close()
    return render(request, 'admin/edit_match_info.html',
                  {'form': form, 'match_id': match_id})


@staff_member_required
def delete_match_info(request, match_id):
    conn = sqlite3.connect('./db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM matchInfo WHERE id = ?", (match_id,))
    conn.commit()
    conn.close()

    return redirect('custom_admin:admin_home')


# 用户视图


def home_view(request):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('./db.sqlite3')

    # 使用 pandas 读取数据
    query = "SELECT * FROM matchInfo"
    pandas_df = pd.read_sql_query(query, conn)

    # 关闭数据库连接
    conn.close()

    # 准备数据并渲染模板
    data = pandas_df.to_dict(orient='records')
    data = {'data': data}
    return render(request, 'prediction/home.html', data)


def select_view(request):
    return render(request, 'prediction/select.html')


def predict_view(request):
    selected_match = request.POST.get('matchSelect', '')
    if selected_match == '':
        home_team = request.POST.get('homeTeam', '')
        away_team = request.POST.get('awayTeam', '')
        home_team = get_key_from_value(country_name, home_team)
        away_team = get_key_from_value(country_name, away_team)
    else:
        home_team, away_team = selected_match.split(
            ' vs ') if ' vs ' in selected_match else ('', '')

    winner, winner_proba = predict_match(home_team, away_team)

    a = '平局'

    if winner != 'Draw':
        a = country_name.get(winner, winner)

    recent_match = get_recent_matches(home_team, away_team)

    context = {
        'winner': a + '(' + winner + ')',
        'winner_proba': winner_proba,
        'recent_match': recent_match
    }

    return render(request, 'prediction/predict.html', context)


def country_display(request):
    return render(request, 'prediction/country.html')
