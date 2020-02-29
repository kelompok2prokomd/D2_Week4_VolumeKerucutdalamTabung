#OOP
#Class
class Identitas:
    __id=0
    __nama=""
    __kelas=""

	
	# function to set data 
    def setData(self,id,nama,kelas):
        self.__id=id
        self.__nama = nama
        self.__kelas = kelas

	
	# function to get/print data
    def showData(self):
        print("Id\t\t:",self.__id)
        print("Nama\t:", self.__nama)
        print("Kelas\t:", self.__kelas)


# main function definition
def main():
    idn=Identitas()
    idn.setData(1,'sibad','7')
    idn.showData()
	
if __name__=="__main__":
    main()

#funcion
def kerucut(tk):
    return 1/3*22/7*r**2*tk
def tabung (r):
    return 22/7*r**2*t
if __name__ == "__main__":

    print("Menghitung Volume Kerucut dalam Tabung dengan jari-jari yang sama \n")
    
    
    tk = int(input("Masukkan tinggi kerucut: "))
    r = int(input("Masukkan jari-jari tabung dan kerucut: "))
    t = int(input("Masukkan tinggi tabung: "))
    

# variable
    a = kerucut(tk)
    b = tabung(r)
    
    
    print("\n")

    print("Volume kerucut adalah = {}".format(a))
    print("Volume tabung adalah = {}".format(b))


#loop
    selisih = [a, b]
    sum = 0
#iterasi
    for each in selisih:
        sum = b-a
 
    print("Selisih volume tabung dan volume kerucut adalah = {}".format(sum))


# branching 
    threshold = t
    
    if (tk  < (threshold-1)):
      print("karena tinggi kerucut lebih kecil dari tinggi tabung, maka kerucut dapat masuk seluruhnya kedalam tabung".format(r, threshold))
    elif(tk == threshold):
      print("maka kerucut dapat masuk seluruhnya kedalam tabung, dan menyinggung sisi tabung.".format(r, threshold))
    else:
      print("karena tinggi kerucut lebih besar dari jari-jari tabung, maka kerucut tidak dapat masuk seluruhnya kedalam tabung".format(r, threshold)) 
   
