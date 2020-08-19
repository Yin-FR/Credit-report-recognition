<template>
    <div class="demo-image__preview">
        <p></p>
        <el-image
                style="width: 300px; height: 300px"
                :src="examplePicRoute"
                :preview-src-list="[examplePicRoute]"
                >
        </el-image>
    </div>
</template>

<script>
    export default {
        name: "ExamplePicShow",
        props: [
            'examplePicRoute',
            'picTitle'
        ]
    }
</script>

<style scoped>
    img {
        width: 50%;
    }
</style>