import gspread
from oauth2client.service_account import ServiceAccountCredentials


def updatePoms(OBJECTS):

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("tomato_history").sheet1
    
    cell_list = sheet.range(1,1,len(OBJECTS),5)
    ob = 0
    count = 0
    for cell in cell_list:
        if count == 5:
            ob += 1
            count = 0
        att = [OBJECTS[ob].time, OBJECTS[ob].date, OBJECTS[ob].description, OBJECTS[ob].code, OBJECTS[ob].duration]
        cell.value = att[count]
        count += 1

    sheet.update_cells(cell_list)

    return 0
