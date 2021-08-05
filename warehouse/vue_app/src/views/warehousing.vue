<template>
    <div class="page">
        <!-- <span>page</span> -->
        <div class="from_info">
            <el-form ref="form" :model="form" :rules="rules" label-width="120px">
                <el-form-item label="ID" prop="id">
                    <el-input v-model="form.id"></el-input>
                </el-form-item>
                <el-form-item label="出厂编号起" prop="start_numbering">
                    <el-input v-model="form.start_numbering"></el-input>
                </el-form-item>
                <el-form-item label="出厂编号止" prop="stop_numbering">
                    <el-input v-model="form.stop_numbering"></el-input>
                </el-form-item>
                <el-form-item label="产品型号" prop="model">
                    <el-select v-model="form.model" placeholder="选择电表型号" clearable style="width:100%">
                        <el-option label="DDS250" value="DDS250"></el-option>
                        <el-option label="DDS250M" value="DDS250M"></el-option>
                        <el-option label="DTS980" value="DTS980"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="生产厂家" prop="factory">
                    <el-input v-model="form.factory"></el-input>
                </el-form-item>
                <el-form-item label="生产日期" prop="date">
                    <el-date-picker
                    v-model="form.date"
                    type="datetime"
                    placeholder="选择日期时间">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="使用年限" required>
                    <el-input-number v-model="form.years"  :min="1" :max="30"></el-input-number>
                </el-form-item>
                <el-form-item label="鉴定周期" required>
                    <el-input-number v-model="form.cycle"  :min="1" :max="30"></el-input-number>
                </el-form-item>
                <el-form-item label="鉴定人" prop="appraiser">
                    <el-select v-model="form.appraiser" clearable placeholder="请选择">
                        <el-option label="管理员1" value="管理员1"></el-option>
                        <el-option label="管理员2" value="管理员2"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="鉴定日期" prop="appraisal_date">
                    <el-date-picker
                    v-model="form.appraisal_date"
                    type="datetime"
                    placeholder="选择日期时间">
                    </el-date-picker>
                </el-form-item>
            </el-form>
        </div>
        <div>
            <el-button class="el_but" type="primary" @click="add_list('form')">确定入库</el-button>
        </div>

    </div>
</template>
<script>
import * as api from "../api/api";
export default {
    data(){
        return{
            form:{
                id:"",
                start_numbering:'',
                stop_numbering:'',
                model:'',
                factory:"",
                date:"",
                years:'10',
                cycle:"",
                appraiser:"",
                appraisal_date:"",
            },
            rules:{
                id:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 5, message: '长度在 1 到 5 个字符', trigger: 'blur' }
                ],
                start_numbering:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur' }
                ],
                stop_numbering:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 30, message: '长度在 1 到 30 个字符', trigger: 'blur' }
                ],
                model:[
                     { required: true, message: '请至少选择一个有效值', trigger: 'change' }
                ],
                factory:[
                    { required: true, message: '请输入有效值', trigger: 'blur' },
                    { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
                ],
                date:[
                    { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
                ],
                appraiser:[
                    { required: true, message: '请至少选择一个有效值', trigger: 'change' }
                ],
                appraisal_date:[
                    { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
                ]
            }
        }
    },
    methods:{
        add_list(formName){
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    api.add_info(this.form).then(res => {
                        console.log(res)
                        this.form={}
                        this.$message.success("操作成功")
                    })
                } else {
                    return false;
                }
            });
        }
    }
}
</script>
<style scoped>
    .page{
        padding: 5px 10px;
         display: flex;
    }
    .from_info{
        width: 500px;
    }
    .el_but{
        margin-top: 558px;
    }
</style>