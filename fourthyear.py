import pandas as pd


def fourth(batch):
    index_col_2_yr = "B.TECH. IV Yr.(VII SEMESTER) TIMETABLE, ODD SEMESTER 2018 (COMBINED) JIIT128(Effective from 18/07/2018)"

    timetable = pd.read_excel("timetable4.xlsx", index_col=index_col_2_yr)
    # sperating cols

    timetable.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    timetable.columns.name = " "

    # seprating days

    mon = timetable.loc["MON":"TUE"].iloc[:-1]
    tue = timetable.loc["TUE":"WED"].iloc[:-1]
    wed = timetable.loc["WED":"THUR"].iloc[:-1]
    thu = timetable.loc["THUR":"FRI"].iloc[:-1]
    fri = timetable.loc["FRI":"SAT"].iloc[:-1]
    sat = timetable.loc["SAT":].iloc[:-1]

    days = [mon, tue, wed, thu, fri, sat]

    classdict = {'P': 'Practical', 'L': 'Lecture', 'T': 'Tutorial'}

    lecturerDict = {}

    subjectdict = {}

    rows = []

    for i in range(len(days)):  # Number of days
        print('For ', list(days[i][1]))  #
        newlist = []
        for j in range(1, 10):  # Number of classes per day
            classes_in_slot = list(days[i][j].dropna())
            haveClasses = [i for i in range(len(classes_in_slot)) if
                           batch in classes_in_slot[i] or 'ALL' in classes_in_slot[i]]
            toShow = ''
            for hc in haveClasses:
                temp = classes_in_slot[hc].replace("\n", "")
                for cls in temp.split(', '):
                    typeofclass = cls[0]
                    roomNum = cls[cls.index('-') + 1:cls.index('/')] if (('-') in cls and ('/') in cls) else ""
                    subject = cls[cls.index('(') + 1:cls.index(')')] if ('(' in cls and (')') in cls) else ""
                    lecturer = cls[cls.index('/') + 1:] if (('-') in cls and ('/') in cls) else ""

                    typeofclass = classdict[cls[0]] if typeofclass in classdict else typeofclass
                    subject = subjectdict[subject] if subject in subjectdict else subject
                    lecturer = lecturerDict[lecturer] if lecturer in lecturerDict else lecturer

                    clsDetails = '[' + typeofclass + '][' + subject + '][' + roomNum + '][' + lecturer + ']'
                    toShow += clsDetails + '~'

                # print('toShow is ', toShow)
            newlist.append(toShow[:-1])
            # print('newlist is \n', newlist,'\n')
        rows.append(newlist)

    final = pd.DataFrame(rows, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], columns=timetable.iloc[0])
    final.columns.name = "Days/Time"

    return final.transpose().to_dict('list')

# e4 = fourth('E4')
#
# for k in e4.keys():
#     print(k, '->', e4[k])
