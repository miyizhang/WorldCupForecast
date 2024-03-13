from joblib import load
import pandas as pd

team_stats_raw = pd.read_csv('data/team_stats_raw.csv')

gb = load('model/gradient_boosting_model.joblib')


def find_stats(team_1):
    # team_1 = "Qatar"
    past_games = team_stats_raw[(team_stats_raw["team"] == team_1)].sort_values("date")
    last5 = team_stats_raw[(team_stats_raw["team"] == team_1)].sort_values("date").tail(5)

    team_1_rank = past_games["rank"].values[-1]
    team_1_goals = past_games.score.mean()
    team_1_goals_l5 = last5.score.mean()
    team_1_goals_suf = past_games.suf_score.mean()
    team_1_goals_suf_l5 = last5.suf_score.mean()
    team_1_rank_suf = past_games.rank_suf.mean()
    team_1_rank_suf_l5 = last5.rank_suf.mean()
    team_1_gp_rank = past_games.points_by_rank.mean()
    team_1_gp_rank_l5 = last5.points_by_rank.mean()

    return [team_1_rank, team_1_goals, team_1_goals_l5, team_1_goals_suf, team_1_goals_suf_l5, team_1_rank_suf,
            team_1_rank_suf_l5, team_1_gp_rank, team_1_gp_rank_l5]


def find_features(team_1, team_2):
    rank_dif = team_1[0] - team_2[0]
    goals_dif = team_1[1] - team_2[1]
    goals_dif_l5 = team_1[2] - team_2[2]
    goals_suf_dif = team_1[3] - team_2[3]
    goals_suf_dif_l5 = team_1[4] - team_2[4]
    goals_per_ranking_dif = (team_1[1] / team_1[5]) - (team_2[1] / team_2[5])
    dif_rank_agst = team_1[5] - team_2[5]
    dif_rank_agst_l5 = team_1[6] - team_2[6]
    dif_gp_rank = team_1[7] - team_2[7]
    dif_gp_rank_l5 = team_1[8] - team_2[8]

    return [rank_dif, goals_dif, goals_dif_l5, goals_suf_dif, goals_suf_dif_l5, goals_per_ranking_dif, dif_rank_agst,
            dif_rank_agst_l5, dif_gp_rank, dif_gp_rank_l5, 1, 0]


def predict_match(home_team, away_team, model='gb'):
    home_stats = find_stats(home_team)
    away_stats = find_stats(away_team)
    features_g1 = find_features(home_stats, away_stats)
    features_g2 = find_features(away_stats, home_stats)

    probs_g1 = gb.predict_proba([features_g1])
    probs_g2 = gb.predict_proba([features_g2])

    team_1_prob_g1 = probs_g1[0][0]
    team_1_prob_g2 = probs_g2[0][1]
    team_2_prob_g1 = probs_g1[0][1]
    team_2_prob_g2 = probs_g2[0][0]

    team_1_prob = (probs_g1[0][0] + probs_g2[0][1]) / 2
    team_2_prob = (probs_g2[0][0] + probs_g1[0][1]) / 2

    draw = False

    if ((team_1_prob_g1 > team_2_prob_g1) & (team_2_prob_g2 > team_1_prob_g2)) | (
            (team_1_prob_g1 < team_2_prob_g1) & (team_2_prob_g2 < team_1_prob_g2)):
        draw = True
    elif team_1_prob > team_2_prob:
        winner = home_team
        winner_proba = team_1_prob
    elif team_2_prob > team_1_prob:
        winner = away_team
        winner_proba = team_2_prob

    if draw == False:
        # print(" %s vs. %s: %s 获胜，胜率： %.2f" % (home_team, away_team, winner, winner_proba))
        return winner, winner_proba
    else:
        return 'Draw', 0.5
