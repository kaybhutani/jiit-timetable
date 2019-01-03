import pandas as pd
import xlrd

def second(batch):
   
    index_col_2_yr="B.TECH. II Yr.(IV SEMESTER TIMETABLE)EVEN SEMESTER 2019(Combined) JIIT128(Eff. FROM 03/01/2019)"

    data=pd.read_excel("timetable2.xlsx", index_col=index_col_2_yr)
    #sperating cols

    data.columns=[1,2,3,4,5,6,7,8,9]

    data.columns.name=" "

    #seprating days

    mon=data.loc["MON":"TUE"].iloc[:-1]
    tue=data.loc["TUE":"WED"].iloc[:-1]
    wed=data.loc["WED":"THURSDAY"].iloc[:-1]
    thu=data.loc["THURSDAY":"FRI"].iloc[:-1]
    fri=data.loc["FRI":"SAT"].iloc[:-1]
    sat=data.loc["SAT":].iloc[:-1]



    #list of df
    data2=[mon,tue,wed,thu,fri,sat]

    final=data.dropna()
    #data2
    #final=data.dropna()
    #final
    #edit data frame here . make first row the column labels

    rows=[]


    #realgame
    #move all to class and fns

    for i in range (0,6):
        newlist=[]
        for j in range(1,10):
            new=data2[i][j].dropna()
            new2=new.str.contains(batch)
            new3=new.str.contains('ALL')
            new2=new2|new3
            if not ((new[new2]).empty):
                temp=new[new2].tolist()[0].replace("\n","")
                
                #comment to show subject code
                # temp1=temp.find('(')
                # temp2=temp.find(')')
                # temp=temp[:temp1]+temp[temp2+1:]
                #comment to show subject code
                
                temp3=temp.find('/')
                temp=temp[:temp3]
                newlist.append(temp)
                #method 2
                #newlist.append(new[new2].tolist().replace('\n',''))
            else:
                newlist.append(" ")
        rows.append(newlist)

        
    #final.append(new[new2])
    #final

    final=pd.DataFrame(rows,index=["Mon","Tue","Wed","Thu","Fri","Sat"],columns=data.iloc[0])
    final.columns.name="Days/Time"

    return(final.transpose().to_dict('list'))
