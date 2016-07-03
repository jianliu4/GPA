#encoding=utf-8


class Calculate:

    total_gpa = 0.0
    temp_grade = 0.0
    total_credit = 0.0

    def __init__(self):
        self.total_gpa = 0.0
        self.total_credit = 0.0

    def calculate(self, grades, credit):
        print "计算"
        for i in range(len(grades)):
            if grades[i] == "优":
                self.total_gpa += credit[i] * 3.9
            elif grades[i] == "良":
                self.total_gpa += credit[i] * 3.0
            elif grades[i] == "中":
                self.total_gpa += credit[i] * 2.0
            elif grades[i] == "及格":
                self.total_gpa += credit[i] * 1.2
            elif grades[i] == "不及格":
                self.total_gpa += credit[i] * 0
            elif float(grades[i]) >= 95:
                self.total_gpa += credit[i] * 4.3
            elif float(grades[i]) >= 90:
                self.total_gpa += credit[i] * 4.0
            elif float(grades[i]) >= 85:
                self.total_gpa += credit[i] * 3.7
            elif float(grades[i]) >= 82:
                self.total_gpa += credit[i] * 3.3
            elif float(grades[i]) >= 78:
                self.total_gpa += credit[i] * 3.0
            elif float(grades[i]) >= 75:
                self.total_gpa += credit[i] * 2.7
            elif float(grades[i]) >= 72:
                self.total_gpa += credit[i] * 2.3
            elif float(grades[i]) >= 68:
                self.total_gpa += credit[i] * 2.0
            elif float(grades[i]) >= 66:
                self.total_gpa += credit[i] * 1.7
            elif float(grades[i]) >= 64:
                self.total_gpa += credit[i] * 1.3
            elif float(grades[i]) >= 60:
                self.total_gpa += credit[i] * 1.0
            else:
                self.total_gpa += credit[i] * 0
            self.total_credit += credit[i]

        return self.total_gpa/self.total_credit







