<template>
    <div>
        <v-app-bar fixed
                   color="#804877"
                   dark
                   shrink-on-scroll
                   prominent
                   fade-img-on-scroll
                   scroll-threshold="500">
            <template v-slot:img="{ props }">
                <v-img v-bind="props"
                       gradient="to top right, rgba(55,236,186,.7), rgba(25,32,72,.7)">
                </v-img>
            </template>

            <v-app-bar-title><div>Allocation & Utilization</div></v-app-bar-title>

            <v-spacer></v-spacer>

            <template v-slot:extension>
                <v-tabs align-with-title>
                    <v-tab>Team</v-tab>
                    <v-tab>Allocation</v-tab>
                    <v-tab>Utilization</v-tab>
                </v-tabs>
            </template>

        </v-app-bar>
    </div>
</template>

<script>

    export default {
        name: 'NavBar'
    };

</script>