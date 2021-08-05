<template>
    <!-- <div class="page_login">
        <div class="login_box">
            <h2>登录</h2>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <el-button type="primary" plain    style="margin:10px 0;" @click="to_link()">登录</el-button>

        </div>
 
    </div>     -->
    <div class="page">
        <div class="login_box">
            <h2>登录</h2>
            
            <el-form ref="form" :model="form">
                <el-input v-model="form.name" placeholder="名称"></el-input>
                <el-input v-model="form.password" placeholder="密码" show-password></el-input>
            </el-form>
            <el-button type="primary" plain    style="margin:30px 0;" @click="to_link()">登录</el-button>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                form:{
                    name:'admin',
                    password:'',
                },
                input:''
            }
        },
        computed:{

        },
        methods: {
            to_link(){
                if(this.form.password == '') return this.$message.error('请输入内容');
                sessionStorage.setItem("value", this.form.name);
                this.$router.push("/");
            }
        },
    }
</script>
<style scoped>
    .page{
        width: 100%;
        height: 100%;
        background: #2d3a4b;
         position: fixed;
    }
    .login_box{
        color: azure;
        width: 400px;
        text-align: center;
        margin: 50px auto;
    }
    .login_box >>> .el-input{
        margin-top: 30px;
    }
</style>