if __name__ == "__main__":
   f = open("origen.txt")
   g = open("destino.txt","w")
   for linea in f:
      g.write(linea)
   g.close()
   f.close()



if __name__ == "__main__":
   f = open("origen.txt")
   g = open("destino.txt","w")
   linea = f.readline()
   while linea != "":
      g.write(linea)
      linea = f.readline()
   g.close()
   f.close()
