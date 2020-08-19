<template>
    <div>
        <div>
            <div v-if="this.introduction">
                <p class="demonstration">使用说明</p>
                <el-carousel trigger="click" :height="this.has - 166 + 'px'">

                    <el-carousel-item v-for="(item, index) in this.introduction" :key="index">
                        <h2>第{{index + 1}}步</h2>
                        <h3 class="small">{{ item.text }}</h3>
                        <img :src="item.img" height="70%" width="60%"/>
                    </el-carousel-item>
                </el-carousel>
            </div>
        </div>
    </div>
</template>

<script>
    import Editor from "./Editor";
    export default {
        name: "IntroPage",
        components: {Editor},
        data(){
            return{
                has: window.innerHeight,
                introduction:[
                    {text: "查看示例图片要求", img: require("../assets/introImg_0.png")},
                    {text: "根据示例图片上传符合要求的清晰图片", img: require("../assets/introImg_1.png")},
                    {text: "上传完成后点击识别，提交成功后等待10秒左右", img: require("../assets/introImg_2.png")}
                ]
            }
        }
    }
</script>

<style scoped>
    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 50px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
</style>