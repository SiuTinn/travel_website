<template>
    <base-nav class="main-nav flex-row align-items-md-center navbar-horizontal" effect="light" expand type="">
        <a aria-label="Bootstrap" class="navbar-brand mr-0 mr-md-2" href="/"
           slot="brand">
            <img src="https://demos.creative-tim.com/vue-argon-dashboard/img/brand/white.png">
            <sup>Docs</sup>
        </a>

        <div class="row" slot="content-header" slot-scope="{closeMenu}">
            <div class="col-6 collapse-brand">
                <a href="/">
                    <img src="https://demos.creative-tim.com/vue-argon-dashboard/img/brand/white.png">
                </a>
            </div>
            <div class="col-6 collapse-close">
                <close-button @click="closeMenu"></close-button>
            </div>
        </div>

        <ul class="navbar-nav flex-row mr-auto ml-4 d-none d-md-flex">
            <li class="nav-item">
                <a class="nav-link" href="https://demos.creative-tim.com/vue-argon-dashboard/#/">Live Preview</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://github.com/creativetimofficial/vue-argon-dashboard/issues"
                   target="_blank">Support</a>
            </li>
        </ul>
        <div class="d-none d-sm-block ml-auto">
            <ul class="navbar-nav ct-navbar-nav flex-row align-items-center">
                <li class="nav-item dropdown d-none">
                    <a aria-expanded="false" aria-haspopup="true" class="btn-link text-white dropdown-toggle mr-sm-3"
                       data-toggle="dropdown" href="#" id="ct-versions">1.0</a>
                    <div aria-labelledby="ct-versions" class="dropdown-menu">
                        <a class="dropdown-item active" href="../../docs/1.0/">Latest - 1.0</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://www.facebook.com/creativetim" target="_blank">
                        <i class="fab fa-facebook-square"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://twitter.com/creativetim" target="_blank">
                        <i class="fab fa-twitter"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://www.instagram.com/creativetimofficial"
                       target="_blank">
                        <i class="fab fa-instagram"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://dribbble.com/creativetim"
                       target="_blank">
                        <i class="fab fa-dribbble"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-icon" href="https://www.github.com/creativetimofficial"
                       target="_blank">
                        <i class="fab fa-github"></i>
                    </a>
                </li>
            </ul>
        </div>
        <SearchBox v-if="$site.themeConfig.search !== false"/>
<<<<<<< HEAD
        <a class="btn btn-neutral btn-icon ml-sm-3 d-none d-md-block" href="https://www.creative-tim.com/product/vue-argon-dashboard"
=======
        <a class="btn btn-neutral btn-icon ml-sm-3 d-none d-md-block"
           href="https://www.creative-tim.com/product/vue-argon-dashboard"
>>>>>>> frontend
           target="_blank">
      <span class="btn-inner--icon">
        <i class="fa fa-cloud-download mr-2"></i>
      </span>
            <span class="nav-link-inner--text">Download</span>
        </a>
    </base-nav>
</template>
<script>
    import SearchBox from '../../node_modules/vuepress/lib/default-theme/SearchBox.vue';

    export default {
        components: {
            SearchBox
        }
    }
</script>
<style lang="scss">
    nav.main-nav {
        z-index: 50;

        &.navbar {
            background-color: #41B883;
            box-shadow: rgba(116, 129, 141, .1) 0 1px 1px 0;
            position: fixed;

            .container {
                max-width: 100%;
                width: 100%;
            }

            .navbar-brand,
            .navbar-brand:hover {
                color: white;
            }
        }

        &.navbar .nav-link {
            color: white !important;

            &:hover {
                border: 0 !important;
                margin: 0 !important;
            }

            &.router-link-active {
                color: white !important;
                border-bottom: 2px solid white !important;
            }
        }

        &.navbar .search-box .suggestion a {
            color: inherit;
        }
    }
</style>
