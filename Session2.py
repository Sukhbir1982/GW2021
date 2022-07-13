johnsAge = 22
print("Johns Age is :", johnsAge)
print("Hashtag of Johns Age is ", id(johnsAge))


jennieAge = 20

siasAge = jennieAge
print("Sias Age is :", siasAge)
print("Hashtag of Sias Age is ", id(siasAge))

#del jennieAge
print("Jennies Age is :", jennieAge)
print("Hashtag of Jennies Age is ", id(jennieAge))

print("Hashtag of Sias Age Binary is ", bin(id(siasAge)))
print("Hashtag of Sias Age Octal is ", oct(id(siasAge)))
print("Hashtag of Sias Age Decimal is ", id(siasAge))
print("Hashtag of Sias Age HexaDecimal is ", hex(id(siasAge)))