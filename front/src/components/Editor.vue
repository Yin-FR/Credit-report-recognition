<template>
    <div>

        <img :src="this.cropImg" alt="上传图片" width="80%"
             v-if="this.$store.state.infoOrStatus[this.index].imagReceived"/>


        <el-button type="primary" plain @click="reUploadImg(index)" v-if="this.cropImg">重新上传</el-button>
        <el-button type="primary" plain @click="dialogVisible = true" v-if="!this.cropImg">图片上传</el-button>
        <el-dialog
                :title="'上传第'+(this.index+1)+'张图片'"
                :visible.sync="dialogVisible"
                :before-close="handleClose"
                width="80%"
        >
            <input ref="input" type="file" name="image" accept="image/*" @change="setImage" v-show="false"/> <!--上传图片文件-->
            <div class="content">
                <div class="cropper-area">
                    <div class="img-cropper" style="margin: 0 auto; width: 80%">
                        <vue-cropper ref="cropper" :src="imgSrc" v-if="cropImg">
                        </vue-cropper>
                    </div>
                    <div class="actions">
                        <el-button type="success" @click.prevent="showFileChooser" style="margin: 10px">选择图片</el-button>
                        <el-button type="success" @click.prevent="cropImage" v-if="imgSrc" style="margin: 10px">确认裁剪</el-button>
                    </div>
                </div>
                <div v-show="this.cropImg">
                    <img alt="cropped img" :src="this.cropImg" style="width: 60% ; height: 60%"/>
                    <p></p>
                    <el-button type="primary" @click="this.submit">提交</el-button>
                </div>
            </div>

            <span slot="footer" class="dialog-footer">
            </span>
        </el-dialog>




    </div>
</template>

<script>
    import VueCropper from 'vue-cropperjs';
    import 'cropperjs/dist/cropper.css';
    export default {
        name: "Editor",
        props: {
            index: Number
        },
        components:{
            VueCropper
        },
        data() {
            return {
                imgSrc: '',
                cropImg: '',
                imgName: '',
                dialogVisible: false
            };
        },
        methods: {
            cropImage() {
                // get image data for post processing, e.g. upload or setting image src
                this.cropImg = this.$refs.cropper.getCroppedCanvas().toDataURL();
                this.imgSrc = this.cropImg
                console.log(typeof this.imgSrc)
                this.$refs.cropper.replace(event.target.result);
            },
            setImage(e) {
                const file = e.target.files[0];
                this.imgName = file.name
                if (file.type.indexOf('image/') === -1) {
                    alert('Please select an image file');
                    return;
                }
                if (typeof FileReader === 'function') {
                    const reader = new FileReader();
                    reader.onload = (event) => {
                        this.imgSrc = event.target.result;
                        this.cropImg = this.imgSrc;
                        if (this.$refs.cropper != null){
                            this.$refs.cropper.replace(event.target.result);
                        }
                    };
                    reader.readAsDataURL(file);
                } else {
                    alert('Sorry, FileReader API not supported');
                }
            },
            showFileChooser() {
                this.$refs.input.click();
            },
            dataURLtoBlob: function(dataurl) {
                let arr = dataurl.split(','),
                    mime = arr[0].match(/:(.*?);/)[1],
                    bstr = atob(arr[1]),
                    n = bstr.length,
                    u8arr = new Uint8Array(n);
                while (n--) {
                    u8arr[n] = bstr.charCodeAt(n);
                }
                return new Blob([u8arr], { type: mime });
            },
            submit() {
                let file = this.dataURLtoBlob(this.cropImg)
                file.name = this.imgName;
                let formData = new FormData();
                formData.append('file', file, this.imgName);
                formData.append('index', this.index.toString())
                let config = {
                    header: {
                        'Content-Type':'multipart/form-data'
                    }
                };
                const axiosAjax = this.axios.create({
                    timeout: 1000*60,
                    withCredentials: true
                });
                axiosAjax.post('http://47.98.136.14:4400/get/data', formData, config).then((res)=> {
                    console.log(res.data);
                    this.info = res.data;
                    this.dialogVisible = false;
                    if (this.info === "成功") {
                        let indexAndFile = {
                            index: this.index,
                            file: file
                        };
                        this.$store.dispatch("uploadImage", {indexAndFile})
                        this.$store.dispatch("uploadVerify", this.index)
                    }
                    this.$notify({
                        title: this.$store.state.infoOrStatus[this.index].imagReceived.name + "上传成功"
                    })
                }).catch((err)=>{
                    console.log(err)
                })
            },
            handleClose(done) {
                this.$confirm('确认关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => {});
            },
            reUploadImg(index) {
                this.dialogVisible = true;
                this.$store.dispatch("reUploadImage", index)
            }
        },
    };
</script>

<style scoped>

</style>