import sys
import csv

class ParseCsv:

    def __init__(self, fh):
        self.__fileHanlder = fh
        self.__data = []

    def Data(self):
        try:
            self.__data = self.__ReadFileHanlder()
            return self.__data

        except TypeError:
            return "Err:: invalid file: None"
        except FileNotFoundError:
            return "Err:: No such file or directory"
        except:
            return "Err:: unhanlded exception..!"

    def __ReadFileHanlder(self):
        
        with open(self.__fileHanlder, newline='') as f:
            reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
            next(reader, None)
            
            title = {}
            gerne = []
            for row in reader:
                title[row[0]] = row[1:]
                for i in row[1:]:
                    gerne.append(i)
            
        data = {}

        for i in set(gerne):
            data[i] = []
            for k, v in title.items():
                if(i in v):
                    data[i].append(k)
        
        del data['']
        #self.__buildTable(data)
        self.__writeToCsv(data)

    def __writeToCsv(self, data):
        for k , v in data.items():
            print(k)
            for i in v:
                print(i)
            print("\n=================\n")
        '''
        with open('data.csv', mode='w') as csv_file:
            fieldnames = list(data.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for k, v in data.items():
                writer.writerows()
            writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
            writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
        '''
    def __buildTable(self, data):

        page ="<!DOCTYPE html><html><head><style> table {  font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}td, th {  border: 1px solid #dddddd; text-align: left; padding: 8px;}tr:nth-child(even) {  background-color: #dddddd;}</style></head><body><h2>HTML Table</h2><table><tr>"
        for i in data.keys():
            page += "<th>"+i+"</th>"
        page += "</tr>"#<tr>"
        '''
        counter = 0
        maxV = len(max(data.values(),key=len))
        for k, v in data.items():
            for i in v:
                page += "<td>"+i+"</td>"
                counter += 1
            
            for i in range(maxV-counter):
                print("--")
                page += "<td></td>"

            page += "</tr>"
        '''    
        page += "</table></body></html>"

        print(page)
        


    def __OldbuildTable(self, data):

        page ="<!DOCTYPE html><html><head><style> table {  font-family: arial, sans-serif;  border-collapse: collapse;  width: 100%;}td, th {  border: 1px solid #dddddd; text-align: left; padding: 8px;}tr:nth-child(even) {  background-color: #dddddd;}</style></head><body><h2>HTML Table</h2><table><tr>"
        for i in data.keys():
            page += "<th>"+i+"</th>"
        page += "</tr><tr>"
        

        for k, v in data.items():
            for i in v:
                #print(i)
                page += "<td>"+i+"</td>"
            page += "</tr>"

        page += "</table></body></html>"

        print(page)
if __name__ == "__main__":
    fh = sys.argv[1]
    parse = ParseCsv(fh)
    parse.Data()



'''
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
</table></body></html>
'''
















'''
    def __ReadFileHanlder(self):
        
        with open(self.__fileHanlder, newline='') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
            next(reader, None)
            gernes = []
            movies= {}

            for row in reader:
                moveGerne = []

                for i in row[2].split('|'):
                    gernes.append(i)
                    moveGerne.append(i)
                    
                movies[row[1]] = moveGerne
            for i in set(gernes):
                print(i)
            ''
            data = {}
            for i in set(gernes):
                data[i] = []
                for k, v in movies.items():
                    if i in v:
                        data[i].append(k) 

            #self.__data = set(gernes)
            print(data)
            ''
'''