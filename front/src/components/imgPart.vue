<template>
    <div>
        <div id="ifOne" v-if="indexR===0">
            <ExamplePicShow :example-pic-route="$store.state.infoOrStatus[0].exampleImg"
                        :pic-title="'示例图片1'" v-if="!this.$store.state.infoOrStatus[0].uploadFinishedStatus"/>
        </div>
        <div id="ifTwo" v-if="indexR===1">
            <ExamplePicShow :example-pic-route="$store.state.infoOrStatus[1].exampleImg"
                            :pic-title="'示例图片2'" v-if="!this.$store.state.infoOrStatus[1].uploadFinishedStatus"/>
        </div>

    </div>
</template>

<script>
    import ExamplePicShow from "./ExamplePicShow";
    export default {
        name: "ImgPart",
        props:['indexRec'],
        components: {ExamplePicShow},
        computed: {
            indexR(){
                if(this.indexRec === 'one'){
                    return 0
                }else if (this.indexRec === 'two'){
                    return 1
                }else {
                    return 2
                }
            }
        }
    }
</script>

<style scoped>

</style>