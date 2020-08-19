/*
    状态对象模块
 */

export default {

    recoginzeResults:[
        [],
        []
    ],
    infoOrStatus:[
        {
            recFinishedStatus: false,
            uploadFinishedStatus: false,
            reserveAllStatus: false,
            exampleImg: require('../assets/reportImg0.png'),
            imagReceived: null
        },
        {
            recFinishedStatus: false,
            uploadFinishedStatus: false,
            reserveAllStatus: false,
            exampleImg: require('../assets/reportImg1.png'),
            imagReceived: null
        }
    ],
    recogntionResults:{
        fromImgOne: {},
        fromImgTwo: {}
    }
}