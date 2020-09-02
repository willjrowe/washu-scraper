from firebase import firebase

firebase = firebase.FirebaseApplication("https://washu-scrape.firebaseio.com/",None)

data = {
    "Name" : "Jack",
    "OtherName" : "Jill"
}

# result = firebase.post("washu-scrape/test",data)
# print(result)

getResult = firebase.patch("/users/other",data)
print(getResult)