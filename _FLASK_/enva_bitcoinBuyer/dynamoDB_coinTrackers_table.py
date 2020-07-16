import boto3

dynamodb=boto3.resource('dynamodb')
dynamoTable=dynamodb.Table('coinTrackers')
dynamoTable.put_item(
    Item = {
      "id": 4,
      "user_id":"4",
      "name":"Thomas Milton",
      "firstName": "Thomas",
      "lastName":" Maestas",
      "email": "thomas@gmail.com",
      "phone":"5055087707",
      "contactType": "email",
      "userGroup": "2",
      "groupName": "CoinTrader",
      "dateOfBirth": "1976/09/03",
      "isActive": "true",
      "photoPath": "assets\/images\/d.png"
    }
)
