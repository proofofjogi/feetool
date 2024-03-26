/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "na1vxtv87bxfjm4",
    "created": "2024-03-26 15:43:52.816Z",
    "updated": "2024-03-26 15:43:52.816Z",
    "name": "fee_data",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "hdlh3tlu",
        "name": "data",
        "type": "json",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "maxSize": 2000000
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("na1vxtv87bxfjm4");

  return dao.deleteCollection(collection);
})
