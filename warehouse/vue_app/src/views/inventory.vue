<template>
  <div class="page">
    <el-button type="primary" plain icon="el-icon-circle-plus-outline" style="margin-bottom:10px" >添加出库</el-button>
    <el-table :data="tableData" style="width: 100%" border>
      <el-table-column prop="id" label="ID" width="50px"  align="center"></el-table-column>
      <el-table-column prop="inventory_number" label="货物编号" align="center" min-width="100px">
        <template slot-scope="scope" >
          
          <span>{{scope.row.inventory_number}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="inventory_model" label="货物型号" align="center">
        <template slot-scope="scope" >
          
          <span>{{scope.row.inventory_model}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="model" label="数量" align="center" width="80px">
        <template slot-scope="scope" >
          <span>{{scope.row.number}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="date" label="出库时间" align="center">
        <template slot-scope="scope" >
          
          <span>{{scope.row.date|dateFormat}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="univalent" label="单价" align="center">
        <template slot-scope="scope" >
          
          <span>{{scope.row.univalent}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="order_number" label="订单号" align="center" min-width="120px">
        <template slot-scope="scope" >
          
          <span>{{scope.row.order_number}}</span>
        </template>
      </el-table-column>
      <el-table-column prop="amount" label="金额" align="center">
        <template slot-scope="scope" >
          <span>{{scope.row.amount}}</span>
        </template>
      </el-table-column>
    <el-table-column prop="operating_user" label="操作人" align="center">
        <template slot-scope="scope" >
          <span>{{scope.row.operating_user}}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作" align="center">
        <template slot-scope="scope">
            <el-button type="danger" icon="el-icon-delete" circle size="mini" @click="del_info(scope.row)"></el-button>
        </template>

      </el-table-column>
    </el-table>

  </div>
</template>
<script>
import * as api from "../api/api";
// import * as fecha from 'element-ui/lib/utils/date';
export default {
  data() {
    return {
      tableData: [],
      is_show:false
    };
  },
  mounted() {
    
    this.inventory_info()
    
  },
  methods: {

    //出库列表信息
    inventory_info(){
        api.inventory_info().then(res => {
            this.tableData = res.data
            console.log(res);
        });
    },

    //删除信息
    del_info(){
      
    }

  }
};
</script>
<style scoped>
.page {
  padding: 5px 10px;
}
</style>
