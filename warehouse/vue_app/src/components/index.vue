<template>
    <div class="page">
        <el-menu
            router
            :default-active="active_index"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
          <el-menu-item index="/">人员管理</el-menu-item>
          <el-submenu index='1'>
              <template slot="title">设备管理</template>
              <el-menu-item index="/electric_meter">电表信息</el-menu-item>
              <el-menu-item index="/warehousing">设备入库</el-menu-item>
              <el-menu-item index="/inventory">设备出库</el-menu-item>
          </el-submenu>
          <el-submenu index='2'>
              <template slot="title">其他</template>
              <el-menu-item index="/H">订单查询</el-menu-item>
          </el-submenu>
          <div class="login">
            <el-button type="" plain size="mini"   style="float: right;margin-top:15px;" @click="login()">退出</el-button>
          </div>
        </el-menu>
        <transition name="slide" mode="out-in">
            <router-view/>
        </transition>
        
    </div>
</template>

<script>
export default {
  name: "index",
  data() {
      return {
          active_index : ''
      };
    },
    mounted: function () {
      this.active_index = this.$route.path
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
        login(){
              sessionStorage.clear();
              this.$router.push('/login')
      },
    },

}
</script>

<style scoped>
  .page >>> .el-menu.el-menu--horizontal{
    padding: 0 10px;
  }
          .slide-enter-active,
        .slide-leave-active {
                will-change: transform;
                transition: all .5s ease;
        }
        .slide-enter {
                opacity: 0;
                transform: translateX(-30px);

        } 
        .slide-leave-active {
                opacity: 0;
                transform: translateX(30px);
                display: none;
        }
</style>