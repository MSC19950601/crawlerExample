class Output(object):
    def __init__(self):
        self.datas = []

    def collectData(self, newData):
        if newData is None:
            return
        self.datas.append(newData)


    def outputUrl(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('gbk'))
            fout.write("<td>%s</td>" % data['title'].encode('gbk'))
            fout.write("<td>%s</td>" % data['summary'].encode('gbk'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()
