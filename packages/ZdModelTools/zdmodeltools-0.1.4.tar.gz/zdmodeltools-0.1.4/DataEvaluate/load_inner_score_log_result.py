import pandas as pd

def main():
    scores_name_list = ['rh','xiaoniu','xys','v7plus','hn','bairong','biyu','dxm_cx_score',
                            'main_a_fpd10_v1','main_a_fpd10_v2','main_a_cpd10_v1','main_a_cpd10_v2','main_a_spd10_v1',
                            'zx_a_fpd10_v1','zx_a_cpd10_v1','zx_a_cpd10_v2','zx_a_spd10_v1',
                            'hn_a_fpd10_v1','hn_a_spd10_v1','br_a_fpd10_v1',
                            'blz_ar_v1']
    df = get_fsample_id()
    df['task_id'] = df['task_id'].astype(str)
    for score in scores_name_list:
        connection = get_database_connection()
        df_t = get_one_score_result(connection, score)
        df_t.drop_duplicates(subset='task_id',keep='first',inplace=True)
        df_t['task_id'] = df_t['task_id'].astype(str)
        df = pd.merge(df, df_t, on='task_id', how='left')
    return df


def get_fsample_id():
    connection = get_database_connection()
    sql = f"""
    SELECT CAST(credit_task_id AS CHAR) AS task_id
    FROM
        (SELECT *, ROW_NUMBER()OVER(PARTITION BY user_identity_id ORDER BY loan_pay_time ASC) AS rn
        FROM bmd_rc_view.risk_contract_info_view rciv 
        WHERE contract_status > 0
        AND credit_task_id IS NOT NULL
        AND loan_task_id IS NOT NULL)a
    WHERE a.rn = 1
    """
    df = get_data(connection, sql)

    return df


def get_one_score_result(connection, score):
    if score == 'rh':
        df = get_data(connection, sql_rh)
    elif score == 'xiaoniu':
        df = get_data(connection, sql_xiaoniu)
    elif score == 'xys':
        df = get_data(connection, sql_xys)
    elif score == 'v7plus':
        df = get_data(connection, sql_v7plus)
    elif score == 'hn':
        df = get_data(connection, sql_hn)
    elif score == 'bairong':
        df = get_data(connection, sql_bairong)
    elif score == 'biyu':
        df = get_data(connection, sql_biyu)
    elif score == 'dxm_cx_score':
        df = get_data(connection, sql_dxm_cx_score)
    elif score == 'main_a_fpd10_v1':
        df = get_data(connection, sql_main_a_fpd10_v1)
    elif score == 'main_a_fpd10_v2':
        df = get_data(connection, sql_main_a_fpd10_v2)
    elif score == 'main_a_cpd10_v1':
        df = get_data(connection, sql_main_a_cpd10_v1)
    elif score == 'main_a_cpd10_v2':
        df = get_data(connection, sql_main_a_cpd10_v2)
    elif score == 'main_a_spd10_v1':
        df = get_data(connection, sql_main_a_spd10_v1)
    elif score == 'zx_a_fpd10_v1':
        df = get_data(connection, sql_zx_a_fpd10_v1)
    elif score == 'zx_a_cpd10_v1':
        df = get_data(connection, sql_zx_a_cpd10_v1)
    elif score == 'zx_a_cpd10_v2':
        df = get_data(connection, sql_zx_a_cpd10_v2)
    elif score == 'zx_a_spd10_v1':
        df = get_data(connection, sql_zx_a_spd10_v1)
    elif score == 'hn_a_fpd10_v1':
        df = get_data(connection, sql_hn_a_fpd10_v1)
    elif score == 'hn_a_spd10_v1':
        df = get_data(connection, sql_hn_a_spd10_v1)
    elif score == 'br_a_fpd10_v1':
        df = get_data(connection, sql_br_a_fpd10_v1)
    elif score == 'blz_ar_v1':
        df = get_data(connection, sql_blz_ar_v1)
    return df


def get_database_connection():
    import pymysql
    username = 'bmd_rc_wangzhiyu'
    password = 'wangzhiyu@bmd'

    db_4000 = pymysql.connect(
        host = '172.16.31.54'
        , port = 4000
        , user = username
        , password = password
        , database = 'bmd_rc_base'
        , autocommit=True  # 启用 autocommit
        , charset = 'utf8'
    )
    return db_4000


def get_data(connection, sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(result, columns=columns)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        connection.close()
        
    return df


# 融慧FA_rm5
sql_rh = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.FA_rm5
FROM bmd_rc_ana.RongHui_FA_rm5_backtest_result_20241014 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.id = rei.id),
online_data AS
(SELECT DISTINCT(redsm.task_id), src.data_creditscore AS FA_rm5
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_237 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=237)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
SELECT * FROM online_data
"""

sql_xiaoniu = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.xiaoniu_scorec1, a.xiaoniu_scorec3
FROM bmd_rc_ana.XiaoNiuScore_backtest_result_20241023 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.id = rei.id),
online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.resultbody_xiaoniu_scorec1 AS xiaoniu_scorec1
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_228 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=228),
online_data2 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.resultbody_xiaoniu_scorec3 AS xiaoniu_scorec3
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_229 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=229)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
(SELECT online_data1.*, online_data2.xiaoniu_scorec3 FROM online_data1
LEFT JOIN online_data2 ON online_data1.task_id = online_data2.task_id)
"""


sql_xys = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.score AS mm082
FROM bmd_rc_ana.XYS_MM082_backtest_result_20240920 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.id = rei.id),
online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.response_data_mingmou_score82 AS mm082
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_225 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=225)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
SELECT online_data1.* FROM online_data1
"""

sql_v7plus = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.score AS v7plus
FROM bmd_rc_ana.HL_V7Plus_backtest_result_20241008 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.id = rei.id),
online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.data_tzedz_ae_v5 AS v7plus
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_226 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=226)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
SELECT online_data1.* FROM online_data1
"""


sql_hn = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.ppcm_behav_score AS ppcm_behav_score
FROM bmd_rc_ana.HN_ppcm_behav_score_20240918 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.id = rei.id),
online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.ppcm_behav_score AS ppcm_behav_score
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_222 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=222)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
SELECT online_data1.* FROM online_data1
"""


sql_bairong = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.scorecust AS scorecust, a.sd_scorecust_score_ywpro AS sd_scorecust_score_ywpro
FROM bmd_rc_ana.BR_lianhe_rongan_scores_20240919 a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON a.input_id = rei.id),
online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.score_scorecust1 AS scorecust, src.scoredata_scorecust1_score_ywpro AS sd_scorecust_score_ywpro
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_220 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=220)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
UNION
SELECT online_data1.* FROM online_data1
"""


sql_biyu = f"""
WITH online_data1 AS
(SELECT DISTINCT(redsm.task_id) AS task_id, src.data_biyu_score64p AS biyu_score64p
FROM bmd_rc_base.risk_engine_data_src_map redsm 
LEFT JOIN bmd_rc_base.data_src_id_155 src ON redsm.data_src_req_id = src.id
WHERE redsm.data_src_id=155)
SELECT * FROM online_data1
"""


sql_main_a_fpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.pred2) AS main_a_fpd10_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 23)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.ronghe_fpd10_model_score_v3_2_20241115_revise_HN_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""


sql_main_a_fpd10_v2 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.pred2) AS main_a_fpd10_v2
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 44)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.ronghe_fpd10_model_score_v2_20241216_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""


sql_main_a_cpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.pred) AS main_a_cpd10_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 40)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.ronghe_cpd10_model_score_v4_20241128_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""

sql_main_a_cpd10_v2 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.pred) AS main_a_cpd10_v2
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 50)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.ronghe_cpd10_model_score_v2_20250113_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""


sql_blz_ar_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.pred) AS blz_ar_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 46)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.M148_XGB_BLZ_AR_v1_20241225_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""



sql_main_a_spd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, b.pred_revised AS main_a_spd10_v1
FROM task_ids
LEFT JOIN bmd_rc_ana.ronghe_spd10_model_score_v1_20250117_ssw b ON CAST(task_ids.task_id AS CHAR) = b.shouxin_task_id 
"""


sql_zx_a_fpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.score) AS zx_a_fpd10_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 24)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.rc_model_test_wn_zx_model_socre_v3_20241119 b ON task_ids.task_id = b.credit_task_id 
"""


sql_zx_a_cpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.score_v1) AS zx_a_cpd10_pred_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 33)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.rc_model_test_wn_zx_cpd10ModelV1_scoreV1_20241126 b ON task_ids.task_id = b.credit_task_id 
"""

sql_zx_a_cpd10_v2 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.M152_XGB_ZX_CPD10_A_v2_20250123) AS zx_a_cpd10_pred_v2
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 56)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.M152_XGB_ZX_CPD10_A_v2_20250123_offline_model_score_20250207 b ON task_ids.task_id = b.credit_task_id 
"""

sql_zx_a_spd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, b.rh_spd10_model_v1 AS zx_a_spd10_v1
FROM task_ids
LEFT JOIN bmd_rc_ana.bmd_rc_model_wn_for_test_spd10_zx_model_v1_data_v1_20250114 b ON task_ids.task_id = b.shouxin_task_id 
"""


sql_hn_a_fpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.HN_fpd10_model_v1_score) AS hn_a_fpd10_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 34)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.M145_XGB_HN_FPD10_V1_20241129_offline_model_score_20241128 b ON task_ids.task_id = b.credit_task_id 
"""


sql_hn_a_spd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, b.hn_spd10_model_score_v1 AS hn_a_spd10_v1
FROM task_ids
LEFT JOIN bmd_rc_ana.HN_spd10_model_score_v1_20250113_wzy b ON task_ids.task_id = b.champion_task_id 
"""

sql_br_a_fpd10_v1 = f"""
WITH task_ids AS
(SELECT task_id FROM bmd_rc_view.risk_credit_apply_view WHERE final_result = 20)
SELECT CAST(task_ids.task_id AS CHAR) AS task_id, COALESCE(a.probability_1_value, b.br_fpd10_model_1218_predict_score) AS br_a_fpd10_v1
FROM task_ids
LEFT JOIN (SELECT task_id, probability_1_value FROM bmd_rc_view.bmd_rc_knowledge_rk_processor_request_log WHERE processor_id = 45)a ON task_ids.task_id = a.task_id
LEFT JOIN bmd_rc_ana.M147_XGB_BR_FPD10_A_V1_20241218_offline_predict_score b ON task_ids.task_id = b.task_id 
"""


sql_dxm_cx_score = f"""
WITH offline_data AS
(SELECT CAST(rei.champion_task_id AS CHAR)AS task_id, a.`小满分（辰星分-互金版高定价V1）` as dxm_cx_score
FROM bmd_rc_test.`20241118_测试结果_朴道_度小满_小满分` a
LEFT JOIN bmd_rc_base.risk_engine_input rei ON CAST(SUBSTRING(a.user_id, 3) AS signed) = rei.id)
SELECT * FROM offline_data WHERE task_id IS NOT NULL
"""
