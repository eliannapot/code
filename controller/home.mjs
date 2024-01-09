const model = await import(`../model/better-sqlite/better-sqlite.mjs`)

export async function showParkingSiteName() {
    try {
        const parkingSiteName = await model.getParkingSiteName()
        console.log('controller', parkingSiteName)
        return parkingSiteName
    } catch(err) {
        console.log(err);
//        res.send(err)
    }
}