<template>
    <div>
        <ImgPart :index-rec="'two'"/>  <!--示例图片展示-->
        <Editor :index="1"/>
        <div>
            <el-button type="default" class="reserve-all-button" @click="recData(1)" v-show="this.$store.state.infoOrStatus[1].imagReceived">识别</el-button>  <!--识别按钮-->
        </div>
        <div v-if="this.$store.state.infoOrStatus[1].recFinishedStatus">   <!--识别结束后，展示结果-->
            <el-table :data="$store.state.recoginzeResults[1]" stripe border width="100%">
                <el-table-column prop="value.item" label="检测项" min-width="20%"></el-table-column>
                <el-table-column label="检测值" min-width="55%">
                    <template slot-scope="scope">
                        <el-input type="textarea" autosize v-model="scope.row.value.itemValue" :disabled="!scope.row.editable"></el-input>
                    </template>
                </el-table-column>
                <el-table-column label="操作" min-width="25%">
                    <template slot-scope="scope">
                        <el-button v-if="scope.row.editable" type="success" size="mini" @click="reserveLineHere(scope.$index)">保存</el-button>
                        <el-button v-if="!scope.row.editable" type="primary" size="mini" @click="editLineHere(scope.$index)">编辑</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <el-button type="success" class="reserve-all-button" @click="reserveAll(1)">保存</el-button>
        </div>
    </div>
</template>

<script>

    import ExamplePicShow from "./ExamplePicShow";
    import ImgPart from "./imgPart";
    import Editor from "./Editor";
    export default {
        name: "RecPageTwo",
        components: {Editor, ImgPart, ExamplePicShow},
        data() {
            return {
            }
        },
        methods: {
            recData(index){
                const h = this.$createElement;
                this.$notify({
                    title:'提交成功',
                    message:h('i', { style: 'color: teal'}, '已提交后台，请耐心等待约10秒'),
                    duration: 3000
                });

                console.log(index);
                const axiosAjax = this.axios.create({
                    timeout: 1000*60,
                    withCredentials: true
                });
                let dataTranversed = [];
                axiosAjax.get("http://47.98.136.14:4400/return/data", {
                    params: {
                        index: index
                    }
                }).then((res)=>{
                    for(let each_key in res.data){
                        dataTranversed.push({key:each_key, value: res.data[each_key], editable: false})
                    }
                    this.$store.dispatch('beginReco', {index, dataTranversed});
                }).catch((err)=>{
                    this.$notify.error({
                        title: '识别失败，请重新刷新页面',
                        message: err,
                        duration: 0
                    })
                    console.log(err);
                });

            },

            editLineHere(index){
                console.log(index);
                this.$store.dispatch('editLine', {indexImg: 1, indexLine: index})
            },

            reserveLineHere(index){
                console.log(index);
                this.$store.dispatch('reserveLine', {indexImg: 1, indexLine: index})
            },

            reserveAll(index){
                this.$notify({
                    title: "成功",
                    message: "结果已保存",
                    type: "success"
                })
                this.$store.dispatch('reserveAllVerify', index)
            }
        }
    }
</script>

<style scoped>
    .reserve-all-button{
        margin: 10px;
    }
</style>