/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("na1vxtv87bxfjm4")

  // remove
  collection.schema.removeField("hdlh3tlu")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "smn1wrqa",
    "name": "target_blocks",
    "type": "number",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "noDecimal": false
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "bldqcaes",
    "name": "fee_rate",
    "type": "number",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "noDecimal": false
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("na1vxtv87bxfjm4")

  // add
  collection.schema.addField(new SchemaField({
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
  }))

  // remove
  collection.schema.removeField("smn1wrqa")

  // remove
  collection.schema.removeField("bldqcaes")

  return dao.saveCollection(collection)
})
