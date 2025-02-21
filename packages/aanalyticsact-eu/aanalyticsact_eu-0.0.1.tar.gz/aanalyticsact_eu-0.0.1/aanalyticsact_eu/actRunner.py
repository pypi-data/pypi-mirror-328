# Created by Youngkwang Cho
# Inquiry : youngkwang.Cho@concentrix.com / ykc124@naver.com
### UK VRS 
from datetime import datetime, timedelta
from calendar import monthrange

def dateConverter(date):
    return datetime.strptime(str(date), '%Y-%m-%d').date()

def lastDayofMonth(date_value):
    return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])

def dateGenerator(startDate, endDate, period):
    start_date = dateConverter(startDate)
    end_date = dateConverter(endDate)

    how_long = (end_date - start_date).days

    if (period == "daily" or period == "Daily"):
        date_list = []
        date_list.append(str(start_date))
        for i in range(how_long):
            start_date += timedelta(days=1)
            start_date_v2 = str(start_date)
            date_list.append(start_date_v2)
        
        return date_list, date_list

    elif (period == "weekly" or period == "Weekly"):
        dateKeep = start_date
        dateKeep_end = dateKeep + timedelta(days=6)

        startDate = []
        endDate = []
        startDate.append(str(dateKeep))
        endDate.append(str(dateKeep_end))

        while dateKeep < end_date:
            dateKeep += timedelta(days=7)
            dateKeep_end += timedelta(days=7)

            startDate.append(str(dateKeep))
            endDate.append(str(dateKeep_end))

        startDate.pop()
        endDate.pop()

        return startDate, endDate

# 230525 revised by Hyunsung Park (Monthly)
    elif (period == "monthly" or period == "Monthly"):
        startDate = []
        endDate = []

        startDate.append(str(start_date))

        startDate_keep = start_date
        endDate_keep = end_date

        while startDate_keep <= lastDayofMonth(end_date):
            if startDate_keep.year == end_date.year and startDate_keep.month == end_date.month:
                # 230601 end date is autofixed to the end of the month
                endDate.append(str(lastDayofMonth(end_date)))
                startDate_keep = endDate_keep + timedelta(days=1)
                startDate.append(str(startDate_keep))
                break

            else:
                endDate_keep = lastDayofMonth(startDate_keep)
                startDate_keep = endDate_keep + timedelta(days=1)
                startDate.append(str(startDate_keep))
                endDate.append(str(endDate_keep))

            startDate_keep = lastDayofMonth(startDate_keep)
        startDate.pop()
        return startDate, endDate

    elif (period == "all" or period == "All"):
        startDate = []
        endDate = []

        startDate.append(str(start_date))
        endDate.append(str(end_date))

        return startDate, endDate
    
    else:
        raise Exception("Type within the followings; daily, weekly, monthly, all")

def rsListGenerator(inputSiteCode, targetRSList):
    finalList = []
    for i in range(len(inputSiteCode)):
        for j in range(len(targetRSList)):
            if inputSiteCode[i] in targetRSList[j]:
                finalList.append(targetRSList[j])

    return finalList


def returnRsList(epp, inputSiteCode):

    defaultEpp = []
    defaultNone = [["uk", "samsungeusssamsung4uk"], ["de", "samsungeusssamsung4de"], ["es", "samsungeusssamsung4es"], ["pt", "samsungeusssamsung4pt"]]

    if epp == True:
        return rsListGenerator(inputSiteCode, defaultEpp)
    else:
        return rsListGenerator(inputSiteCode, defaultNone)


def tbColumnGenerator(tbColumn, if_site_code, breakdown, epp, site_code_rs):
    if site_code_rs == True:
        breakdown = False
        if_site_code = True

    defaultColumn = ["site_code", "period", "start_date", "end_date", "is_epp"]
    if epp == True:
        defaultColumn.insert(1, "breakdown")
        defaultColumn.insert(6, "is_epp_integ")
    else:
        if breakdown == False:
            if if_site_code == True:
                defaultColumn = defaultColumn
            else:
                defaultColumn.insert(1, "dimension")
        
        else:
            if if_site_code == True:
                defaultColumn.insert(1, "breakdown")
            else:
                defaultColumn[0] = "dimension"
                defaultColumn.insert(1, "breakdown")
    
    for i in range(len(tbColumn)):
        defaultColumn.append(tbColumn[i])
    
    return defaultColumn


def tbColumnGeneratorRB(tbColumn, if_site_code, breakdown, epp, site_code_rs):  ##tbColumn, False, False, True, site_code_rs
    if site_code_rs == True:
        breakdown = False
        if_site_code = True
    defaultColumn = ["site_code", "RS ID","Biz_type","Division","Category","Device_type","Date","Channel_Raw"]

  #  defaultColumn = ["site_code", "period", "date", "end_date", "is_epp"]    
    for i in range(len(tbColumn)):
        defaultColumn.append(tbColumn[i])
    
    return defaultColumn