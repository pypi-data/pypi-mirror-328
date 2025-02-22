from radnn import FileStore

oFS = FileStore("MLData")

dTest = {"key1": "value", "key2": "value2"}
dTest["sub"] = { 0: "0", 1 : "1"}

oFS.json.save(dTest, "test.json")

