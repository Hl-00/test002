<template>
  <div class="page">
    <el-table :data="tableData" style="width: 100%" border>
      <el-table-column prop="id" label="ID" width="50px"  align="center"></el-table-column>
      <el-table-column prop="start_numbering" label="出厂编号起" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.start_numbering" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.start_numbering}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="stop_numbering" label="出厂编号止" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.stop_numbering" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.stop_numbering}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="model" label="规格型号" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.model" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.model}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="factory" label="生产厂家" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.factory" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.factory}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="date" label="出厂日期" align="center" :formatter="formDate">
        <template slot-scope="scope" >
          <!-- <el-input v-model="scope.row.date" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input> -->
          <el-date-picker
          size="mini"
          v-model="scope.row.date"
          v-if="!scope.row.is_show"
          type="datetime"
          placeholder="选择日期时间">
          </el-date-picker>
          <span v-if="scope.row.is_show">{{scope.row.date|dateFormat}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="years" label="使用年限" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.years" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.years}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="cycle" label="鉴定周期" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.cycle" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.cycle}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="appraiser" label="鉴定人" align="center">
        <template slot-scope="scope" >
          <el-input v-model="scope.row.appraiser" v-if="!scope.row.is_show" size="mini" placeholder="请输入内容"></el-input>
          <span v-if="scope.row.is_show">{{scope.row.appraiser}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="appraisal_date" label="鉴定日期" align="center" :formatter="formDate">
        <template slot-scope="scope" >
              <el-date-picker
              size="mini"
              v-model="scope.row.appraisal_date"
              v-if="!scope.row.is_show"
              type="datetime"
              placeholder="选择日期时间">
              </el-date-picker>
          <span v-if="scope.row.is_show" :formatter="formDate">{{scope.row.appraisal_date|dateFormat}}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
            <el-button type="primary" plain icon="el-icon-edit" circle size="mini" @click="edit_info(scope.row)"></el-button>
            <el-button type="primary" plain icon="el-icon-circle-check" circle size="mini" @click="edit_save_info(scope.row)"></el-button>
            <el-button type="danger" icon="el-icon-delete" circle size="mini" @click="del_info(scope.row)"></el-button>
        </template>

      </el-table-column>
    </el-table>

  </div>
</template>
<script>
import * as api from "../api/api";
import * as fecha from 'element-ui/lib/utils/date';
export default {
  data() {
    return {
      tableData: [],
      is_show:false
    };
  },
  mounted() {
    
    this.ammeter_list()
    
  },
  methods: {
    formDate(row, column, cellValue){
      return cellValue ? fecha.format(new Date(cellValue), 'yyyy-MM-dd') : '';
    },

    //电表信息
    ammeter_list(){
        api.ammeter_info().then(res => {
            console.log(res.data);
            this.tableData = res.data;
        });
    },

    //编辑信息
    edit_info(row){
      row.is_show = false
    },
    edit_save_info(row){
      // console.log(row)
      api.edit_info(row).then(res => {
        console.log(res)
        this.ammeter_list()
        this.$message.success("操作成功")
      })
      row.is_show = true
    },
    //删除信息
    del_info(row){
      api.delete_info(row.id).then(res =>{
        console.log(res)
        this.$message.success("操作成功")
        this.ammeter_list()
      })
    }

  }
};
</script>
<style scoped>
.page {
  padding: 5px 10px;
}
</style>
