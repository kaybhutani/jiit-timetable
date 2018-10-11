import pandas as pd
<< << << < HEAD


def second(batch):
    index_col_2_yr = "B.TECH. II Yr.(III SEMESTER TIMETABLE) ODD SEMESTER 2018(Combined) JIIT128(Effective from 17/07/2018)"

    timetable = pd.read_excel("timetable2.xlsx", index_col=index_col_2_yr)
    # sperating cols

    timetable.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    timetable.columns.name = " "

    # seprating days

    mon = timetable.loc["MON":"TUE"].iloc[:-1]
    tue = timetable.loc["TUE":"WED"].iloc[:-1]
    wed = timetable.loc["WED":"THURS"].iloc[:-1]
    thu = timetable.loc["THURS":"FRI"].iloc[:-1]
    fri = timetable.loc["FRI":"SAT"].iloc[:-1]
    sat = timetable.loc["SAT":].iloc[:-1]

    days = [mon, tue, wed, thu, fri, sat]

    classdict = {'P': 'Practical', 'L': 'Lecture', 'T': 'Tutorial'}

    lecturerDict = {}

    subjectdict = {}

    rows = []

    for i in range(len(days)):  # Number of days
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

# second('E1')
== == == =

def second(batch):
    index_col_2_yr = "B.TECH. II Yr.(III SEMESTER TIMETABLE) ODD SEMESTER 2018(Combined) JIIT128(Effective from 17/07/2018)"

    data = pd.read_excel("timetable2.xlsx", index_col=index_col_2_yr)
    # sperating cols

    data.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data.columns.name = " "

    # seprating days

    mon = data.loc["MON":"TUE"].iloc[:-1]
    tue = data.loc["TUE":"WED"].iloc[:-1]
    wed = data.loc["WED":"THURS"].iloc[:-1]
    thu = data.loc["THURS":"FRI"].iloc[:-1]
    fri = data.loc["FRI":"SAT"].iloc[:-1]
    sat = data.loc["SAT":].iloc[:-1]

    # list of df
    data2 = [mon, tue, wed, thu, fri, sat]

    final = data.dropna()
    # data2
    # final=data.dropna()
    # final
    # edit data frame here . make first row the column labels

    rows = []

    # realgame
    # move all to class and fns

    for i in range(0, 6):
        newlist = []
        for j in range(1, 10):
            new = data2[i][j].dropna()
            new2 = new.str.contains(batch)
            new3 = new.str.contains('ALL')
            new2 = new2 | new3
            if not ((new[new2]).empty):
                temp = new[new2].tolist()[0].replace("\n", "")

                # comment to show subject code
                # temp1=temp.find('(')
                # temp2=temp.find(')')
                # temp=temp[:temp1]+temp[temp2+1:]
                # comment to show subject code

                temp3 = temp.find('/')
                temp = temp[:temp3]
                newlist.append(temp)
                # method 2
                # newlist.append(new[new2].tolist().replace('\n',''))
            else:
                newlist.append(" ")
        rows.append(newlist)

    # final.append(new[new2])
    # final

    final = pd.DataFrame(rows, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], columns=data.iloc[0])
    final.columns.name = "Days/Time"

    return (final.transpose().to_dict('list'))

>> >> >> > b7c89282744b1e0e9ef97f6d3f38ecee0b045b32
