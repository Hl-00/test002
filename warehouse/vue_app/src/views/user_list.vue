<template>
  <div class="page">
    <el-button type="primary" plain icon="el-icon-circle-plus-outline" style="margin-bottom:10px" @click="add_user">添加</el-button>
    <el-table :data="tableData" style="width: 100%" border >
      <el-table-column prop="id" label="ID" width="180" align="center"></el-table-column>
      <el-table-column prop="username" label="姓名" width="180" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.username" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.username}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="password" label="密码" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.password" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.password}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="root" label="权限" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.root" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.root}}</span>
        </template>
      </el-table-column>
      <el-table-column label="修改" align="center">
        <template slot-scope="scope">
          <el-button type="primary" plain icon="el-icon-edit" circle size="mini" @click="edit_user_info(scope.row)"></el-button>
          <el-button type="primary" plain icon="el-icon-circle-check" circle size="mini" @click="save_user_info(scope.row)"></el-button>
          <el-button type="danger" icon="el-icon-delete" circle size="mini" @click="del_user_info(scope.row)"></el-button>
        </template>

      </el-table-column>
    </el-table>

    <!-- 添加人员信息dialog -->
    <el-dialog
    title="添加信息"
    :visible.sync="dialogVisible"
    width="40%"
    :before-close="handleClose">
      <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="80px" class="demo-ruleForm">
            <el-form-item label="姓名" prop="name">
                <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="ruleForm.password" show-password></el-input>
            </el-form-item>
              <el-form-item label="确认密码" prop="password_s">
                <el-input v-model="ruleForm.password_s" show-password></el-input>
            </el-form-item>
            <el-form-item label="权限" prop="root">
                <el-select v-model="ruleForm.root" clearable placeholder="请选择" style="width:100%">
                    <el-option label="A" value="A"></el-option>
                    <el-option label="B" value="B"></el-option>
                    <el-option label="C" value="C"></el-option>
                    <el-option label="D" value="D"></el-option>
                </el-select>
            </el-form-item>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false" size="mini">取 消</el-button>
        <el-button type="primary" @click="q_add_userinfo('ruleForm')" size="mini">确 定</el-button>
      </span>
  </el-dialog>
    
  </div>
</template>

<script>
import * as api from "../api/api.js";
export default {
  name: "user_list",
  data(){
      return{
          tableData:[],
          dialogVisible : false,
          ruleForm:{
              name:'',
              password:'',
              password_s:'',
              root:"",
          },
          rules:{
                name:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
                ],
                password:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
                ],
                password_s:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
                ],
                root:[
                  { required: true, message: '请至少选择一个有效值', trigger: 'change' }
                ]
          }
      }
  },
  mounted() {
      this.user_info()
  },
  methods:{
    //  人员信息
      user_info(){
          api.user_list().then(res => {
            this.tableData = res.data
            console.log(res);
          });
      },

      // 添加人员信息
      add_user(){
          // let list = [];
          // this.tableData.push(list)
          this.dialogVisible = true
      },
      q_add_userinfo(formName){
            this.$refs[formName].validate((valid) => {
                if (valid) {
                  if(this.ruleForm.password != this.ruleForm.password_s) return this.$message.error("两次密码不一样")
                  api.add_user_info(this.ruleForm).then(res => {
                    console.log(res)
                    this.$message.success("操作成功")
                    this.user_info()
                    this.dialogVisible = false
                    this.ruleForm = {}
                  })
                  
                } else {
                    return false;
                }
            });
      },
      handleClose(){
          this.dialogVisible = false
          this.ruleForm = {}
      },
      // 删除人员信息
      del_user_info(row){
        api.del_user_info(row.id).then(res => {
          console.log(res)
          this.$message.success("操作成功")
          this.user_info()
        })
      },
      // 编辑人员信息
      edit_user_info(row){
        row.is_show = false
      },
      save_user_info(row){
        row.is_show = true
        api.edit_userlist_info(row).then(res => {
          console.log(res)
          this.$message.success("操作成功")
          this.user_info()
        })
      }

  }
};
</script>

<style scoped>
.page {
  margin: 5px 10px;
}
</style>