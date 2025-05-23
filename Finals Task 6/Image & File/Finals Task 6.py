use mongo_practice
switched to db mongo_practice
db["movies"].find()
db.movies.insertOne({title:"Fight Club", writer: "Chuck Palahniuk", year: "1999", actors:["Brad Pitt", "Edward Norton"]})
{
  acknowledged: true,
  insertedId: ObjectId('6828a66416bbbaac4f77cf72')
}
db.movies.insertOne({title:"Pulp Fiction", writer:"Quentin Tarantino", year:"2009", actors:["John Travolta", "Uma Thurman"]})
{
  acknowledged: true,
  insertedId: ObjectId('6828a67516bbbaac4f77cf73')
}
db.movies.insertOne({title:"Inglorious Basterds", writer:"Quentin Tarantino", year:"2009", actors:["Brad Pitt", "Diane Kruger", "Eli Roth"]})
{
  acknowledged: true,
  insertedId: ObjectId('6828a69516bbbaac4f77cf74')
}
db.movies.insertOne({title:"The Hobbit:An unexpected Journey", writer:"J.R.R. Tolkein", year:"2012",franchise:"The Hobbit"})
{
  acknowledged: true,
  insertedId: ObjectId('6828a6b016bbbaac4f77cf75')
}
db.movies.insertOne({title:"The Hobbit: The Desolation of Smaug",
writer:"J.R.R Tolkien", year:"2013", franchise:"The Hobbit"})
{
  acknowledged: true,
  insertedId: ObjectId('6828a6c516bbbaac4f77cf76')
}
db.movies.insertOne({title:"The Hobbit: The Battle of the Five Armies", writer:"J.R.R Tolkien", year:"2002", franchise:"The Hobbit", synopsis:"Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness."})
{
  acknowledged: true,
  insertedId: ObjectId('6828a6d416bbbaac4f77cf77')
}
db.movies.insertOne({title:"Pee Wee Herman's Big Adventures"})
{
  acknowledged: true,
  insertedId: ObjectId('6828a72316bbbaac4f77cf78')
}
db.movies.insertOne({title:"Avatar"})
{
  acknowledged: true,
  insertedId: ObjectId('6828a73416bbbaac4f77cf79')
}
db.movies.find()
{
  _id: ObjectId('6828a66416bbbaac4f77cf72'),
  title: 'Fight Club',
  writer: 'Chuck Palahniuk',
  year: '1999',
  actors: [
    'Brad Pitt',
    'Edward Norton'
  ]
}
{
  _id: ObjectId('6828a67516bbbaac4f77cf73'),
  title: 'Pulp Fiction',
  writer: 'Quentin Tarantino',
  year: '2009',
  actors: [
    'John Travolta',
    'Uma Thurman'
  ]
}
{
  _id: ObjectId('6828a69516bbbaac4f77cf74'),
  title: 'Inglorious Basterds',
  writer: 'Quentin Tarantino',
  year: '2009',
  actors: [
    'Brad Pitt',
    'Diane Kruger',
    'Eli Roth'
  ]
}
{
  _id: ObjectId('6828a6b016bbbaac4f77cf75'),
  title: 'The Hobbit:An unexpected Journey',
  writer: 'J.R.R. Tolkein',
  year: '2012',
  franchise: 'The Hobbit'
}
{
  _id: ObjectId('6828a6c516bbbaac4f77cf76'),
  title: 'The Hobbit: The Desolation of Smaug',
  writer: 'J.R.R Tolkien',
  year: '2013',
  franchise: 'The Hobbit'
}
{
  _id: ObjectId('6828a6d416bbbaac4f77cf77'),
  title: 'The Hobbit: The Battle of the Five Armies',
  writer: 'J.R.R Tolkien',
  year: '2002',
  franchise: 'The Hobbit',
  synopsis: 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
}
{
  _id: ObjectId('6828a72316bbbaac4f77cf78'),
  title: "Pee Wee Herman's Big Adventures"
}
{
  _id: ObjectId('6828a73416bbbaac4f77cf79'),
  title: 'Avatar'
}
db.movies.find({writer:"Quentin Tarantino"})
{
  _id: ObjectId('6828a67516bbbaac4f77cf73'),
  title: 'Pulp Fiction',
  writer: 'Quentin Tarantino',
  year: '2009',
  actors: [
    'John Travolta',
    'Uma Thurman'
  ]
}
{
  _id: ObjectId('6828a69516bbbaac4f77cf74'),
  title: 'Inglorious Basterds',
  writer: 'Quentin Tarantino',
  year: '2009',
  actors: [
    'Brad Pitt',
    'Diane Kruger',
    'Eli Roth'
  ]
}
db.movies.find({actors:"Brad Pitt"})
{
  _id: ObjectId('6828a66416bbbaac4f77cf72'),
  title: 'Fight Club',
  writer: 'Chuck Palahniuk',
  year: '1999',
  actors: [
    'Brad Pitt',
    'Edward Norton'
  ]
}
{
  _id: ObjectId('6828a69516bbbaac4f77cf74'),
  title: 'Inglorious Basterds',
  writer: 'Quentin Tarantino',
  year: '2009',
  actors: [
    'Brad Pitt',
    'Diane Kruger',
    'Eli Roth'
  ]
}
db.movies.find({franchise:"The Hobbit"})
{
  _id: ObjectId('6828a6b016bbbaac4f77cf75'),
  title: 'The Hobbit:An unexpected Journey',
  writer: 'J.R.R. Tolkein',
  year: '2012',
  franchise: 'The Hobbit'
}
{
  _id: ObjectId('6828a6c516bbbaac4f77cf76'),
  title: 'The Hobbit: The Desolation of Smaug',
  writer: 'J.R.R Tolkien',
  year: '2013',
  franchise: 'The Hobbit'
}
{
  _id: ObjectId('6828a6d416bbbaac4f77cf77'),
  title: 'The Hobbit: The Battle of the Five Armies',
  writer: 'J.R.R Tolkien',
  year: '2002',
  franchise: 'The Hobbit',
  synopsis: 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
}
db.movies.find({year:{$gt:"1990", $lt:"2000"}})
{
  _id: ObjectId('6828a66416bbbaac4f77cf72'),
  title: 'Fight Club',
  writer: 'Chuck Palahniuk',
  year: '1999',
  actors: [
    'Brad Pitt',
    'Edward Norton'
  ]
}
db.movies.find({$or:[{year:{$gt:"2010"}},{year: {$lt:"2000"}}]})
{
  _id: ObjectId('6828a66416bbbaac4f77cf72'),
  title: 'Fight Club',
  writer: 'Chuck Palahniuk',
  year: '1999',
  actors: [
    'Brad Pitt',
    'Edward Norton'
  ]
}
{
  _id: ObjectId('6828a6b016bbbaac4f77cf75'),
  title: 'The Hobbit:An unexpected Journey',
  writer: 'J.R.R. Tolkein',
  year: '2012',
  franchise: 'The Hobbit'
}
{
  _id: ObjectId('6828a6c516bbbaac4f77cf76'),
  title: 'The Hobbit: The Desolation of Smaug',
  writer: 'J.R.R Tolkien',
  year: '2013',
  franchise: 'The Hobbit'
}
db.movies.update({_id:ObjectId("5c9f98e5e5c2dfe9b3729bfe")}, {$set:{synopsis:"A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}})
DeprecationWarning: Collection.update() is deprecated. Use updateOne, updateMany, or bulkWrite.
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
db.movies.update({_id:ObjectId("5c9fa42ae5c2dfe9b3729c03")}, {$set:{synopsis:"The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
db.movies.update({_id:ObjectId("5c9f983ce5c2dfe9b3729bfc")}, {$push:{actors:"Samuel L. Jackson"}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
db.movies.find({synopsis:{$regex:"Bilbo"}})
{
  _id: ObjectId('6828a6d416bbbaac4f77cf77'),
  title: 'The Hobbit: The Battle of the Five Armies',
  writer: 'J.R.R Tolkien',
  year: '2002',
  franchise: 'The Hobbit',
  synopsis: 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
}
db.movies.find({synopsis:{$regex:"Gandalf"}})
db.movies.find({synopsis:{$regex:"Gandalf"}})
db.movies.find({$and:[{synopsis:{$regex:"Bilbo"}}, {synopsis:{$not:/Gandalf/}}]}
SyntaxError: Unexpected token, expected "," (1:80)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mmovies[33m.[39mfind({$and[33m:[39m[{synopsis[33m:[39m{$regex[33m:[39m[32m"Bilbo"[39m}}[33m,[39m {synopsis[33m:[39m{$not[33m:[39m[35m/Gandalf/[39m}}]}
 [90m   |[39m                                                                                 [31m[1m^[22m[39m[0m
db.movies.find({$and:[{synopsis:{$regex:"Bilbo"}},{synopsis:{$not:/Gandalf/}}]}
SyntaxError: Unexpected token, expected "," (1:79)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mmovies[33m.[39mfind({$and[33m:[39m[{synopsis[33m:[39m{$regex[33m:[39m[32m"Bilbo"[39m}}[33m,[39m{synopsis[33m:[39m{$not[33m:[39m[35m/Gandalf/[39m}}]}
 [90m   |[39m                                                                                [31m[1m^[22m[39m[0m
db.movies.find({$or:[{synopsis:{$regex:"dwarves"}}, {synopsis:{$regex:"hobbit"}}]})
db.movies.find({$and:[{synopsis:{$regex:"gold"}}, {synopsis:{$regex:"dragon"}}]})
db.movies.remove({_id:ObjectId("5c9f992ae5c2dfe9b3729c00")})
DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.
{
  acknowledged: true,
  deletedCount: 0
}
db.movies.remove({_id:ObjectId("5c9f9936e5c2dfe9b3729c01")})
{
  acknowledged: true,
  deletedCount: 0
}
db.users.insertOne({_id:1,username:"GoodGuyGreg", first_name:"Good Guy", last_name:"Greg"})
{
  acknowledged: true,
  insertedId: 1
}
db.users.insert({_id:2, username:"ScumbagSteve", fullname:{first: "Scumbag", last:"Steve"}})
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
{
  acknowledged: true,
  insertedIds: {
    '0': 2
  }
}
db.posts.insert({username:"GoodGuyGreg", title:"Passes out at Party", body:"Raises your credit score"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ab8a16bbbaac4f77cf7a')
  }
}
db.posts.insert({ username:"GoodGuyGreg", title:"Steals your identity", body:"Raises your credit score"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ab9316bbbaac4f77cf7b')
  }
}
db.posts.insert({username:"GoodGuyGreg", title:"Reports a bug in your code", body:"Sends you a pull request"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ab9e16bbbaac4f77cf7c')
  }
}
db.posts.insert({ username:"ScumbagSteve", title:"Borrows something", body:"Sells it"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828abd216bbbaac4f77cf7d')
  }
}
db.posts.insert({ username:"ScumbagSteve", title:"Borrows everything", body:"The end"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828abdf16bbbaac4f77cf7e')
  }
}
db.posts.insert({username:"ScumbagSteve", title:"Forks your repo on github", body:"Sets to private"})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828abeb16bbbaac4f77cf7f')
  }
}
db.comments.insert({ username:"GoodGuyGreg", comment:"Hope you got a good deal!", post:ObjectId("5ca0b7e96435f98b5901f463")})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ac4116bbbaac4f77cf80')
  }
}
db.comments.insert({username:"GoodGuyGreg", comment:"What's mine is yours!", post:ObjectId("5ca0b9706435f98b5901f46a")})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ac4f16bbbaac4f77cf81')
  }
}
db.comments.insert({username:"GoodGuyGreg", comment:"Don't violate the licensing agreement!", post:ObjectId("5ca0b8766435f98b5901f467")})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ac5a16bbbaac4f77cf82')
  }
}
db.comments.insert({username:"ScumbagSteve", comment:"It still isn't clean", post:ObjectId("5ca0b8546435f98b5901f466")})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ac8916bbbaac4f77cf83')
  }
}
db.comments.insert({username:"ScumbagSteve", comment:"Denied your PR cause I found a hack", post:ObjectId("5ca0b9256435f98b5901f469")})
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6828ac9616bbbaac4f77cf84')
  }
}
db.users.find().pretty()
{
  _id: 1,
  username: 'GoodGuyGreg',
  first_name: 'Good Guy',
  last_name: 'Greg'
}
{
  _id: 2,
  username: 'ScumbagSteve',
  fullname: {
    first: 'Scumbag',
    last: 'Steve'
  }
}
db.posts.find().pretty()
{
  _id: ObjectId('6828ab8a16bbbaac4f77cf7a'),
  username: 'GoodGuyGreg',
  title: 'Passes out at Party',
  body: 'Raises your credit score'
}
{
  _id: ObjectId('6828ab9316bbbaac4f77cf7b'),
  username: 'GoodGuyGreg',
  title: 'Steals your identity',
  body: 'Raises your credit score'
}
{
  _id: ObjectId('6828ab9e16bbbaac4f77cf7c'),
  username: 'GoodGuyGreg',
  title: 'Reports a bug in your code',
  body: 'Sends you a pull request'
}
{
  _id: ObjectId('6828abd216bbbaac4f77cf7d'),
  username: 'ScumbagSteve',
  title: 'Borrows something',
  body: 'Sells it'
}
{
  _id: ObjectId('6828abdf16bbbaac4f77cf7e'),
  username: 'ScumbagSteve',
  title: 'Borrows everything',
  body: 'The end'
}
{
  _id: ObjectId('6828abeb16bbbaac4f77cf7f'),
  username: 'ScumbagSteve',
  title: 'Forks your repo on github',
  body: 'Sets to private'
}
db.posts.find({username:"GoodGuyGreg"})
{
  _id: ObjectId('6828ab8a16bbbaac4f77cf7a'),
  username: 'GoodGuyGreg',
  title: 'Passes out at Party',
  body: 'Raises your credit score'
}
{
  _id: ObjectId('6828ab9316bbbaac4f77cf7b'),
  username: 'GoodGuyGreg',
  title: 'Steals your identity',
  body: 'Raises your credit score'
}
{
  _id: ObjectId('6828ab9e16bbbaac4f77cf7c'),
  username: 'GoodGuyGreg',
  title: 'Reports a bug in your code',
  body: 'Sends you a pull request'
}
db.posts.find({username:"ScumbagSteve"})
{
  _id: ObjectId('6828abd216bbbaac4f77cf7d'),
  username: 'ScumbagSteve',
  title: 'Borrows something',
  body: 'Sells it'
}
{
  _id: ObjectId('6828abdf16bbbaac4f77cf7e'),
  username: 'ScumbagSteve',
  title: 'Borrows everything',
  body: 'The end'
}
{
  _id: ObjectId('6828abeb16bbbaac4f77cf7f'),
  username: 'ScumbagSteve',
  title: 'Forks your repo on github',
  body: 'Sets to private'
}
db.comments.find().pretty()
{
  _id: ObjectId('6828ac4116bbbaac4f77cf80'),
  username: 'GoodGuyGreg',
  comment: 'Hope you got a good deal!',
  post: ObjectId('5ca0b7e96435f98b5901f463')
}
{
  _id: ObjectId('6828ac4f16bbbaac4f77cf81'),
  username: 'GoodGuyGreg',
  comment: "What's mine is yours!",
  post: ObjectId('5ca0b9706435f98b5901f46a')
}
{
  _id: ObjectId('6828ac5a16bbbaac4f77cf82'),
  username: 'GoodGuyGreg',
  comment: "Don't violate the licensing agreement!",
  post: ObjectId('5ca0b8766435f98b5901f467')
}
{
  _id: ObjectId('6828ac8916bbbaac4f77cf83'),
  username: 'ScumbagSteve',
  comment: "It still isn't clean",
  post: ObjectId('5ca0b8546435f98b5901f466')
}
{
  _id: ObjectId('6828ac9616bbbaac4f77cf84'),
  username: 'ScumbagSteve',
  comment: 'Denied your PR cause I found a hack',
  post: ObjectId('5ca0b9256435f98b5901f469')
}
db.comments.find({username:"GoodGuyGreg"})
{
  _id: ObjectId('6828ac4116bbbaac4f77cf80'),
  username: 'GoodGuyGreg',
  comment: 'Hope you got a good deal!',
  post: ObjectId('5ca0b7e96435f98b5901f463')
}
{
  _id: ObjectId('6828ac4f16bbbaac4f77cf81'),
  username: 'GoodGuyGreg',
  comment: "What's mine is yours!",
  post: ObjectId('5ca0b9706435f98b5901f46a')
}
{
  _id: ObjectId('6828ac5a16bbbaac4f77cf82'),
  username: 'GoodGuyGreg',
  comment: "Don't violate the licensing agreement!",
  post: ObjectId('5ca0b8766435f98b5901f467')
}
db.comments.find({username:"ScumbagSteve"})
{
  _id: ObjectId('6828ac8916bbbaac4f77cf83'),
  username: 'ScumbagSteve',
  comment: "It still isn't clean",
  post: ObjectId('5ca0b8546435f98b5901f466')
}
{
  _id: ObjectId('6828ac9616bbbaac4f77cf84'),
  username: 'ScumbagSteve',
  comment: 'Denied your PR cause I found a hack',
  post: ObjectId('5ca0b9256435f98b5901f469')
}


