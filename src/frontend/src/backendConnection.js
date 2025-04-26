import { status } from './const';
import axios from 'axios';
import qs from 'qs';
import { backend } from './backend_config';

// 改名为 backend_conn
export const backend_conn = function (api_name, data, that, success, fail, withAuthorization = true) {
    let remote = backend.remote; // 注意这里也要用 backend.remote

    function response_handler(response, that, success, fail) {
        // console.log(response);
        if (response.status === 200) {
            if (response.data.status === status["normal"]) {
                success(response);
            } else if (response.data.status === that.$status['user_authorization_error']) {
                window.alert('用户登录信息有误, 请重新登录');
                that.$session.destroy();
                that.$router.push('/login');
            } else if (response.data.status === that.$status['user_session_timeout']) {
                window.alert('用户长时间未操作, 自动退出, 请重新登录');
                that.$session.destroy();
                that.$router.push('/login');
            } else {
                fail(response);
            }
        } else {
            // console.error('网络连接有问题', response.data);
        }
    }

    function err_handler(/* err */) {
        // 可以在这里处理错误，比如弹窗提示
        // alert('请求出错');
    }

    function data_wrapper(data, that, withAuthorization) {
        if (withAuthorization) {
            if (that.$session.exists()) {
                data.user_id = that.$session.get('user_id');
                data.session_id = that.$session.id().replace('sess:', '');
            } else {
                window.alert('用户已退出, 请重新登录');
                that.$router.push('/login');
            }
        }
        return qs.stringify(data, { arrayFormat: 'repeat' });
    }

    return axios.post(remote + api_name, data_wrapper(data, that, withAuthorization)).then(
        function (response) {
            response_handler(response, that, success, fail);
        }
    ).catch(
        function (err) {
            err_handler(err);
        });
};
