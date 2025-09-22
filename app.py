from flask import Flask, render_template, request, redirect, url_for
import os

from Carbon import perfect_area, radians_index, ba_carbon, dbh_type, allometric, calculate_C

# Helper to safely convert form values to float
def safe_float(val, default=0.0):
    try:
        return float(val)
    except (ValueError, TypeError):
        return default

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        calc_type = request.form.get('calc_type')
        result = None
        table = []
        if calc_type == 'perfect_area':
            s = safe_float(request.form.get('s'))
            e = safe_float(request.form.get('e'))
            n = perfect_area(s, e)
            table = [['ค่าส่วนเบี่ยงเบนมาตรฐาน', s], ['ค่าความคลาดเคลื่อนที่ยอมรับได้', e], ['จำนวนที่ต้องไปสำรวจเพิ่ม', n]]
        elif calc_type == 'radians_index':
            R = int(request.form.get('R', 1))
            D_P = safe_float(request.form.get('D_P'))
            D_P_all = safe_float(request.form.get('D_P_all'))
            total = radians_index(R, D_P, D_P_all)
            table = [['ประเภทดัชนี', R], ['ค่าตัวตั้ง', D_P], ['ค่าตัวหาร', D_P_all], ['ค่าดัชนี', total]]
        elif calc_type == 'ba_carbon':
            DBH = safe_float(request.form.get('DBH'))
            ba = ba_carbon(DBH)
            table = [['ค่าเส้นรอบวง (DBH)', DBH], ['ค่าดูดซับค่าบอนต้นไม้บางชนิด', ba]]
        elif calc_type == 'dbh_type':
            DBH = safe_float(request.form.get('DBH'))
            height = safe_float(request.form.get('height'))
            tree_type = dbh_type(DBH, height)
            table = [['ค่าเส้นรอบวง (DBH)', DBH], ['ความสูง (height)', height], ['ชนิด', tree_type]]
        elif calc_type == 'allometric':
            DBH = safe_float(request.form.get('DBH'))
            height = safe_float(request.form.get('height'))
            forest = int(request.form.get('forest', 1))
            bamboo_type = request.form.get('bamboo_type')
            bamboo_type = int(bamboo_type) if bamboo_type else None
            w_ab = allometric(DBH, height, forest, bamboo_type)
            table = [['ค่าเส้นรอบวง (DBH)', DBH], ['ความสูง (height)', height], ['ประเภทป่า', forest], ['ชนิดไผ่', bamboo_type if bamboo_type else '-'], ['มวลชีวภาพโดยเฉลี่ย', w_ab]]
        elif calc_type == 'calculate_C':
            DBH = safe_float(request.form.get('DBH'))
            height = safe_float(request.form.get('height'))
            forest = int(request.form.get('forest', 1))
            all_area = safe_float(request.form.get('all_area'))
            bamboo_type = request.form.get('bamboo_type')
            bamboo_type = int(bamboo_type) if bamboo_type else None
            ipcc, keep_all = calculate_C(DBH, height, forest, all_area, bamboo_type)
            table = [['ค่าเส้นรอบวง (DBH)', DBH], ['ความสูง (height)', height], ['ประเภทป่า', forest], ['พื้นที่สำรวจทั้งหมด', all_area], ['ชนิดไผ่', bamboo_type if bamboo_type else '-'], ['อัตราการดูดซัพคาร์บอนเฉลี่ย', ipcc], ['อัตราการกักเก็บคาร์บอนโดยรวม', keep_all]]
        # Always render result.html after calculation
        return render_template('result.html', table=table, calc_type=calc_type)
    # GET request: show main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
