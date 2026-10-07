// Connected textures for the Grubenrahmen through Athena. Written by
// tools/textures/grubenrahmen.py; the tiles are in assets/kronwerke/textures/block/ctm.
ClientEvents.generateAssets('last', event => {
    event.json('kronwerke:models/block/grubenrahmen', {"loader": "athena:athena", "athena:loader": "athena:ctm", "ctm_textures": {"center": "kronwerke:block/ctm/grubenrahmen/center", "empty": "kronwerke:block/ctm/grubenrahmen/empty", "horizontal": "kronwerke:block/ctm/grubenrahmen/horizontal", "vertical": "kronwerke:block/ctm/grubenrahmen/vertical", "particle": "kronwerke:block/ctm/grubenrahmen/center"}})
})
