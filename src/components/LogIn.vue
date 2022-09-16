<template>
    <div>
        <v-app>
            <v-container>
                <v-row style="margin-top:15%;">
                    <v-col></v-col>
                    <v-col>
                        <v-row>
                            <v-col cols="4"><img src="./..\assets\Qordata Watermark.png" class="logo newline" /></v-col>
                            <v-col style="margin-top: 10%;">
                                <h2><em>Allocations Sheet!</em></h2>
                            </v-col>
                        </v-row>
                        <v-form ref="form"
                                v-model="valid"
                                lazy-validation>
                            <v-text-field v-model="password"
                                          :counter="30"
                                          :rules="passwordRules"
                                          label="Password"
                                          :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                                          @click:append="() => (value = !value)"
                                          :type="value ? 'password' : 'text'"
                                          required></v-text-field>

                            <v-text-field v-model="email"
                                          :rules="emailRules"
                                          label="E-mail"
                                          required></v-text-field>

                            <v-tooltip bottom>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn :disabled="!valid"
                                           color="primary"
                                           v-bind="attrs"
                                           v-on="on"
                                           @click="validate(false)">
                                        Login
                                    </v-btn>
                                </template>
                                <span>With great powers, comes great responsibility</span>
                            </v-tooltip>

                            <v-dialog transition="dialog-top-transition"
                                      max-width="600">
                                <template v-slot:activator="{ on, attrs }">
                                    <a v-bind="attrs" v-on="on" style="font-size: small; margin-left: 10%;">New to Allocation Sheets?</a>
                                </template>
                                <template v-slot:default="dialog">
                                    <v-card>
                                        <v-toolbar color="#8B008B" dark>Create your ID</v-toolbar>
                                        <v-card-text>
                                            <h2 class="newline">Welcome to the team!</h2>
                                            <v-row>
                                                <v-form ref="form"
                                                        v-model="new_valid"
                                                        lazy-validation
                                                        class="newline"
                                                        style="margin-left:2%;">
                                                    <v-text-field v-model="password"
                                                                  :counter="30"
                                                                  :rules="passwordRules"
                                                                  label="Password"
                                                                  :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
                                                                  @click:append="() => (value = !value)"
                                                                  :type="value ? 'password' : 'text'"
                                                                  required>
                                                    </v-text-field>

                                                    <v-text-field v-model="email"
                                                                  :rules="emailRules"
                                                                  label="E-mail"
                                                                  required>
                                                    </v-text-field>
                                                </v-form>
                                            </v-row>
                                        </v-card-text>
                                        <v-card-actions class="justify-end">
                                            <v-btn text @click="dialog.value = false">Maybe Later</v-btn>
                                            <v-btn text @click="validate(true); dialog.value = false;" :disabled="!new_valid">Sign me up!</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </template>
                            </v-dialog>
                            <v-snackbar v-model="executionSnack" :timeout="5000" :color="snackColor">
                                {{ snackText }}
                                <template v-slot:action="{ attrs }">
                                    <v-btn v-bind="attrs" text @click="executionSnack = false"> Close </v-btn>
                                </template>
                            </v-snackbar>
                        </v-form>
                    </v-col>
                    <v-col></v-col>
                </v-row>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'LogIn',
        components: {
        },
        data() {
            return {
                // form variables
                backend: "http://localhost:5555",
                valid: true,
                new_valid: true,
                password: '',
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => (v && v.length <= 10) || 'Password must be less than 30 characters',
                ],
                email: '',
                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
                ],
                value: String,
                // snack variables
                executionSnack: false,
                snackColor: '',
                snackText: '',
            }
        },
        methods: {
            // form validation
            validate(status) {
                let credentials = {
                    email: this.email,
                    password: this.password,
                    new_user: status
                };
                axios.post(this.backend + '/login', credentials).then(response => {
                    if (response.status == 200) {
                        this.snackText = 'Welcome!';
                        this.snackColor = 'success';
                        this.executionSnack = true;
                        //this.$emit('isAuthenticated', true);
                        this.$session.start();
                        this.$router.push('/hello');
                    }
                    else if (response.status == 201) {
                        this.snackText = 'Your user has been created. Please login now.';
                        this.snackColor = 'success';
                        this.executionSnack = true;
                    }
                    else {
                        this.snackText = '401 Unauthorized!';
                        this.snackColor = 'error';
                        this.executionSnack = true;
                    }
                }).catch(err => {
                    console.log(err);
                    this.executionSnack = true;
                    this.snackColor = 'error';
                    this.snackText = '401 Unauthorized!';
                });
            }
        }
    };
</script>

