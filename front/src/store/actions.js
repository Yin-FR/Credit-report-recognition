/*
    包含多个间接更新state的方法 对象模块
 */

import {BEGIN_RECOGNIZE, EDIT_INLINE, RESERVE_ALL_VERIFY, RESERVE_INLINE, UPLOAD_VERIFY, UPLOAD_IMAGE, REUPLOAD_IMAGE} from './mutations-type'

export default {
    editLine({commit}, indexs){
        commit(EDIT_INLINE, {indexs});
    },

    reserveLine({commit}, indexs){
        commit(RESERVE_INLINE, {indexs})
    },

    uploadVerify({commit}, index){
        commit(UPLOAD_VERIFY, {index})
    },

    reserveAllVerify({commit}, index){
        commit(RESERVE_ALL_VERIFY, {index})
    },

    beginReco({commit}, index, data){
        commit(BEGIN_RECOGNIZE, {index, data})
    },

    uploadImage({commit}, indexAndFile){
        commit(UPLOAD_IMAGE, {indexAndFile})
    },

    reUploadImage({commit}, index){
        commit(REUPLOAD_IMAGE, {index})
    }
}