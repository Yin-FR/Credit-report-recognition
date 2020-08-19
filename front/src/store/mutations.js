/*
    多个可以直接同步更新状态的方法
 */

import {
    BEGIN_RECOGNIZE,
    EDIT_INLINE,
    RESERVE_ALL_VERIFY,
    RESERVE_INLINE,
    REUPLOAD_IMAGE,
    UPLOAD_IMAGE,
    UPLOAD_VERIFY
} from './mutations-type'

export default {
    [EDIT_INLINE](state, {indexs}){
        state.recoginzeResults[indexs.indexImg][indexs.indexLine].editable = true;
    },

    [RESERVE_INLINE](state, {indexs}){
        state.recoginzeResults[indexs.indexImg][indexs.indexLine].editable = false;
    },

    [UPLOAD_VERIFY](state, {index}){
        console.log('成功更改state')
        state.infoOrStatus[index].uploadFinishedStatus=true;
    },

    [RESERVE_ALL_VERIFY](state,{index}){
        console.log('img结果已保存')
        state.infoOrStatus[index].reserveAllStatus = true;
        if (index === 0) {
            for (let each of state.recoginzeResults[index]) {
                state.recogntionResults.fromImgOne[each.value.item] = each.value.itemValue
            }
        }
        if (index === 1){
            for (let each of state.recoginzeResults[index]) {
                state.recogntionResults.fromImgTwo[each.value.item] = each.value.itemValue
            }
        }
    },

    [BEGIN_RECOGNIZE](state, {index}){
        console.log(index)
        console.log(state.infoOrStatus[index.index])
        state.infoOrStatus[index.index].recFinishedStatus = true;
        state.recoginzeResults[index.index] = Object.values(index)[1];
    },

    [UPLOAD_IMAGE](state, {indexAndFile}){
        console.log(indexAndFile.indexAndFile.index)
        console.log(indexAndFile.indexAndFile.file)
        state.infoOrStatus[indexAndFile.indexAndFile.index].imagReceived = indexAndFile.indexAndFile.file
    },

    [REUPLOAD_IMAGE](state, {index}) {
        state.recoginzeResults[index] = [];
        state.infoOrStatus[index].recFinishedStatus = false;
        state.infoOrStatus[index].imagReceived = false;
        state.infoOrStatus[index].reserveAllStatus = false;
        state.infoOrStatus[index].uploadFinishedStatus = false;
    }
}