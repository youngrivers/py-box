$(document).ready(function () {
    //alert('ok');
    $('#login').click(function () {
        var user=$('#text').val(),
            pwd=$('#password').val(),
            pd={'username':user,'password':pwd};
        $.ajax({
            type:'post',
            url:'/',//post或get的地址
            data:pd,//传输的数据
            cache:false,//不设置缓存
            success:function (data) {//请求成功的回调函数
                alert(data)
            },
            error:function () {//请求失败的函数
                alert('error')
            },
        });
        //alert('用户名：'+user)
    });
});