def perfect_area(s, e):
    """Calculate required sample area based on standard deviation and allowable error."""
    try:
        n = ((2 * s) / e) ** 2
        print(f"จำนวนที่ต้องไปสำรวจเพิ่ม : {n:.2f}")
        return n
    except Exception as ex:
        print("Error in perfect_area:", ex)
        return None


def radians_index(R, D_P, D_P_all):
    """Calculate index value based on type."""
    try:
        if D_P_all == 0:
            print("Error: D_P_all cannot be zero.")
            return None
        total = (D_P / D_P_all) * 100
        print(f"ค่าดัชนี : {total:.2f}")
        return total
    except Exception as ex:
        print("Error in radians_index:", ex)
        return None


def ba_carbon(DBH):
    """Calculate basal area for a given DBH."""
    try:
        ba = (3.14 * (DBH ** 2)) / 4
        print(f"ค่าดูดซับค่าบอนต้นไม้บางชนิด : {ba:.2f}")
        return ba
    except Exception as ex:
        print("Error in ba_carbon:", ex)
        return None


def dbh_type(DBH, height):
    """Determine tree type based on DBH and height. Returns type as string."""
    if DBH < 2:
        return "Bamboo"
    elif DBH < 4.5 and height < 1.30:
        return "ลูกไม้"
    elif DBH < 4.5:
        return "ไม้หนุ่ม"
    elif DBH >= 4.5:
        return "ต้นไม้"
    # เถาวัลย์: DBH >= 2 and height < 1.30 but not caught above
    elif DBH >= 2 and height < 1.30:
        return "เถาวัลย์"
    else:
        return "ไม่ทราบ"


def allometric(DBH, height, forest, bamboo_type=None):
    """Calculate biomass based on allometric equations."""
    D = (DBH ** 2) * height
    w_ab = None
    try:
        if forest == 1:  # ป่าดิบ
            w_s = 0.0509 * (D ** 0.919)
            w_b = 0.00893 * (D ** 0.977)
            w_j = 0.0140 * (D ** 0.669)
            w_ab = w_s + w_b + w_j
        elif forest == 2:  # ป่าเต็ง or เบญ
            w_s = 0.0396 * (D ** 0.9326)
            w_b = 0.003487 * (D ** 1.027)
            w_tc = w_s + w_b
            w_j = ((28.0 / w_tc) + 0.025) ** (-1)
            w_ab = w_s + w_b + w_j
        elif forest == 3:  # ป่าสนเขา
            w_s = 0.02141 * (D ** 0.9814)
            w_b = 0.00002 * (D ** 1.4561)
            w_j = 0.00030 * (D ** 1.0138)
            w_ab = w_s + w_b + w_j
        elif forest == 4:  # ป่าชายเลน
            w_s = 0.05466 * (D ** 0.945)
            w_b = 0.01579 * (D ** 0.9124)
            w_j = 0.0678 * (D ** 0.5806)
            w_ab = w_s + w_b + w_j
        elif forest == 5:  # ป่าปาล์ม
            w_ab = 6.666 + 12.826 * (height ** 0.5)
        elif forest == 6:  # ป่าไผ่
            if bamboo_type is None:
                print("Error: bamboo_type required for forest type 6.")
                return None
            if bamboo_type == 1:
                w_ab = 0.1466 * (DBH ** 0.7187)
            elif bamboo_type == 2:
                w_ab = 0.49522 * (DBH ** 0.8726)
            elif bamboo_type == 3:
                w_ab = 0.17466 * (DBH ** 1.0437)
            elif bamboo_type == 4:
                w_ab = 0.2425 * (DBH ** 1.0751)
            else:
                print("Error: Invalid bamboo_type.")
                return None
        elif forest == 7:  # เถาวัลย์
            w_ab = 0.8622 * (DBH ** 2.0210)
        else:
            print("Error: Invalid forest type.")
            return None
        print(f"มวลชีวภาพโดยเฉลี่ย : {w_ab:.2f}")
        return w_ab
    except Exception as ex:
        print("Error in allometric:", ex)
        return None


def calculate_C(DBH, height, forest, all_area, bamboo_type=None):
    """Calculate average and total carbon absorption."""
    Muan_bio = allometric(DBH, height, forest, bamboo_type)
    if Muan_bio is None:
        print("Error: Biomass calculation failed.")
        return None, None
    ipcc = Muan_bio * 0.47
    keep_all = ipcc * all_area
    print(f"อัตราการดูดซัพคาร์บอนเฉลี่ย : {ipcc:.2f}")
    print(f"อัตราการกักเก็บคาร์บอนโดยรวม : {keep_all:.2f}")
    return ipcc, keep_all


def main():
    print("--- โปรแกรมคำนวณคาร์บอนและชีวภาพ ---")
    while True:
        print("\nเลือกฟังก์ชันที่ต้องการ:")
        print("1. คำนวณพื้นที่สำรวจเพิ่ม (perfect_area)")
        print("2. คำนวณค่าดัชนี (radians_index)")
        print("3. คำนวณพื้นที่หน้าตัด (ba_carbon)")
        print("4. หาชนิดต้นไม้ (dbh_type)")
        print("5. คำนวณมวลชีวภาพ (allometric)")
        print("6. คำนวณการดูดซับคาร์บอน (calculate_C)")
        print("0. ออกจากโปรแกรม")
        choice = input("เลือกหมายเลข: ").strip()
        if choice == "0":
            print("จบการทำงาน")
            break
        elif choice == "1":
            try:
                s = float(input("ค่าส่วนเบี่ยงเบนมาตรฐาน : "))
                e = float(input("ค่าความคลาดเคลื่อนที่ยอมรับได้ : "))
                perfect_area(s, e)
            except Exception as ex:
                print("Error:", ex)
        elif choice == "2":
            try:
                R = int(input("ดัชนีที่ต้องการหา (1-4): "))
                D_P = float(input("ค่าตัวตั้ง : "))
                D_P_all = float(input("ค่าตัวหาร : "))
                radians_index(R, D_P, D_P_all)
            except Exception as ex:
                print("Error:", ex)
        elif choice == "3":
            try:
                DBH = float(input("ค่าเส้นรอบวง (DBH): "))
                ba_carbon(DBH)
            except Exception as ex:
                print("Error:", ex)
        elif choice == "4":
            try:
                DBH = float(input("ค่าเส้นรอบวง (DBH): "))
                height = float(input("ความสูง (height): "))
                dbh_type(DBH, height)
            except Exception as ex:
                print("Error:", ex)
        elif choice == "5":
            try:
                DBH = float(input("ค่าเส้นรอบวง (DBH): "))
                height = float(input("ความสูง (height): "))
                forest = int(input("ประเภทป่า (1-7): "))
                bamboo_type = None
                if forest == 6:
                    bamboo_type = int(input("ชนิดไผ่ (1-4): "))
                allometric(DBH, height, forest, bamboo_type)
            except Exception as ex:
                print("Error:", ex)
        elif choice == "6":
            try:
                DBH = float(input("ค่าเส้นรอบวง (DBH): "))
                height = float(input("ความสูง (height): "))
                forest = int(input("ประเภทป่า (1-7): "))
                all_area = float(input("พื้นที่สำรวจทั้งหมด : "))
                bamboo_type = None
                if forest == 6:
                    bamboo_type = int(input("ชนิดไผ่ (1-4): "))
                calculate_C(DBH, height, forest, all_area, bamboo_type)
            except Exception as ex:
                print("Error:", ex)
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง")


if __name__ == "__main__":
    main()