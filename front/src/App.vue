<template>
    <div id="app">
        <el-container>
            <el-header>识别系统</el-header>   <!--顶部-->
            <el-container>
                <el-aside width="15%">
                    <!--侧边导航栏-->
                    <el-button type="info" plain class="button-1" @click="chosePage(1)">1</el-button>
                    <el-button type="info" plain class="button-1" @click="chosePage(2)">2</el-button>
                    <el-button type="info" plain class="button-1" @click="chosePage(0)">说明</el-button>
                </el-aside>
                <el-container>
                    <el-main>   <!--主界面-->
                        <IntroPage v-show="!pageChosen" style="position: relative;margin-top:10px;"/> <!--介绍页-->
                        <RecPageOne v-show="pageChosen===1"/> <!--识别页1-->
                        <RecPageTwo v-show="pageChosen===2"/> <!--识别页2-->
                    </el-main>
                    <el-footer>     <!--页底-->
                        <div>
                            <el-progress type="circle" :percentage="finishedPercentage"
                                         :width="parseInt('50')" style="margin-top: 4px; float: right" v-if="finishedPercentage !== 100">
                            </el-progress> <!--进度环-->
                            <transition name="fade">
                                <el-button icon="el-icon-upload" type="primary" plain
                                           style="float: right; margin-top: 8px"
                                           v-if="finishedPercentage === 100"
                                           @click.prevent="returnResults">储存</el-button>
                            </transition>
                            <span class="span-in-footer">
                                <el-checkbox v-model="this.$store.state.infoOrStatus[0].reserveAllStatus" disabled>图1</el-checkbox>
                                <el-checkbox v-model="this.$store.state.infoOrStatus[1].reserveAllStatus" disabled>图2</el-checkbox>
                            </span>
                        </div>
                    </el-footer>
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>

<script>


    import RecPageOne from "./components/RecPageOne";
    import RecPageTwo from "./components/RecPageTwo";
    import IntroPage from "./components/IntroPage";
    export default {
        name: 'App',
        components: {IntroPage, RecPageTwo, RecPageOne},
        data() {
            return {
                pageChosen: null,
            }
        },
        computed:{
            finishedPercentage(){ /*计算完成进度百分比*/
                let imageReserveList = [
                    this.$store.state.infoOrStatus[0].reserveAllStatus,
                    this.$store.state.infoOrStatus[1].reserveAllStatus,
                ];
                let imageReservedFinishedList = imageReserveList.filter(v=>(v===true));
                return Math.ceil(imageReservedFinishedList.length/imageReserveList.length*100);
            }

        },

        methods: {
            chosePage(pageIndex){
                this.pageChosen = pageIndex;
            },
            returnResults(){
                let dataObj = JSON.stringify(this.$store.state.recogntionResults);
                let config = {
                    header: {
                        'Content-Type':'application/json'
                    }
                };
                const axiosAjax = this.axios.post('http://47.98.136.14:4400/get/js', dataObj, config).then((res)=>{
                    console.log(res.data)
                    if(res.data === "完成"){
                        this.$notify({
                            title: "成功",
                            message: "上传成功",
                            type: "success"
                        })
                    }
                }).catch((err)=>{
                    console.log(err)})
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 0;
        height: 100%;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 2.0s;
    }
    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    button.button-1 {
        width: 100%;
        margin: 0;
    }

    .el-container {
        height: 100%;
    }

    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
    }

    .el-footer {
        text-align: left !important;
    }

    .el-aside {
        background-color: #D3DCE6;
        color: #333;
        text-align: center;
        line-height: 50%;
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
        line-height: 20px;
        padding: 5px !important;
    }

    body > .el-container {
        margin-bottom: 0;
    }

    .el-container:nth-child(5) .el-aside,
    .el-container:nth-child(6) .el-aside {
        line-height: 260px;
    }

    .el-container:nth-child(7) .el-aside {
        line-height: 320px;
    }

    .el-button + .el-button {
        margin-left: 0 !important;
    }


    .el-checkbox__input.is-disabled+span.el-checkbox__label {
        color: #333333 !important;
        cursor: not-allowed;
    }

    .el-checkbox__input.is-checked+span.el-checkbox__label {
        color: #409EFF !important;
    }

    .span-in-footer{
        float: left;
    }

    .el-checkbox {
        color: #606266;
        font-weight: 500;
        font-size: 14px;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        margin-right: 15px !important;
    }
</style>
