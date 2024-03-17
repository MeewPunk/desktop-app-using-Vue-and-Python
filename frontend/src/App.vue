<template>

    <div class="d-flex align-items-center justify-content-center"
        style="height: 100vh; background-image: linear-gradient(to right, #303b5d, #354575, #3a4f8d, #4058a6, #4862bf, #3969c3, #266fc7, #0075ca, #0074b0, #006f92, #006775, #305d5d);">
        <div style="height: 600px; width: 500px; border-radius: 10px; background-color: rgba(255, 255, 255, 0.1); border:  2px solid rgba(255, 255, 255, 0.2);"
            class="d-flex align-items-center justify-content-center">
            <a-form :model="formState" name="basic" :label-col="{ span: 8 }" :wrapper-col="{ span: 16 }"
                autocomplete="off" @finish="onFinish" @finishFailed="onFinishFailed">
                <h1 style="color: white; padding: 2px; margin : 0px">Login</h1>
                <div
                    style="background-color : white; height : 3px; width : 100px; margin-bottom: 30px; margin-top: 5px;">
                </div>
                <a-form-item name="username" :rules="[{ required: true, message: 'Please input your username!' }]">
                    <a-input
                        style="width: 450px; height: 40px; background-color: rgba(255, 255, 255, 0.726); color: #363636;"
                        v-model:value="formState.username" placeholder="Username" />
                </a-form-item>
                <div class="password">
                    <a-form-item name="password" :rules="[{ required: true, message: 'Please input your password!' }]">
                        <a-input-password
                            style="width: 450px; height: 40px; margin-top: 10px; background-color: rgba(255, 255, 255, 0.726); color: #363636;"
                            v-model:value="formState.password" placeholder="Password" />
                    </a-form-item>
                </div>
                <div class="d-flex justify-content-start pt-2">
                    <a-form-item :wrapper-col="{ offset: 0, span: 16 }">
                        <a-button @click="login()"
                            style="background-color: rgba(255, 255, 255, 0.726); color: #353535; border-radius: 6px; width : 120px; height : 37px; font-size: 17px; font-weight: bold"
                            html-type="submit" :loading="loading">Login</a-button>
                    </a-form-item>
                </div>
            </a-form>
        </div>
    </div>
</template>

<script>

    import axios from 'axios'
    export default {
        data() {
            return {
                port_api : 8080,
                loading: false,
                formState: {
                    username: '',
                    password: ''
                },
            }
        },
        mounted() {
            
        },
        methods: {
            // demo call function python
            async login() {
                try {
                    const url = `http://127.0.0.1:${this.port_api}/v1/login`
                    const json = {}
                    const options = {
                        headers: { 'Authorization': `Bearer token` },
                    }
                    const res = await axios.post(url, json, options)
                    console.log('res ', res.data)
                } catch (error) {
                    console.error(error)
                }
            },
        }
    }
</script>

<style >
    .ant-steps-item-title {
        color: rgb(255 255 255 / 88%) !important;
    }
    .ant-input {
        background-color: rgba(255, 255, 255, 0);
    }

    .ant-progress-text {
        color: #ffffff !important;
    }

    .ant-steps-item-title {
        color: #ffffff !important;
    }

    .ant-input {
        background-color: rgba(255, 255, 255, 0);
    }

    .box-shadow-13 {
        box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
    }
</style>



