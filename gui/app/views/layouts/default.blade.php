<!DOCTYPE html>
<html class="no-js" lang="el-GR">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>
            {{ trim($__env->yieldContent('title')) ? $__env->yieldContent('title').' - ' : '' }}MDI
        </title>

        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        {{ HTML::style('components/ionicons/css/ionicons.min.css') }}
        @yield('css')
        {{ HTML::style('css/screen.css') }}

        {{ HTML::script('components/foundation/js/vendor/modernizr.js') }}
    </head>
    <body class="@yield('body-class')">
        <header class="@yield('header-class')">
            <div class="contain-to-grid">
                <div class="row">
                    <div class="large-12 column">
                        <nav class="top-bar" data-topbar role="navigation">
                            <ul class="title-area">
                                <li class="name">
                                    <h1>
                                        <a href="{{ route('home') }}">MDI</a>
                                    </h1>
                                </li>

                                <li class="toggle-topbar menu-icon">
                                    <a href="#"><span>MENU</span></a>
                                </li>
                            </ul>

                            <section class="top-bar-section">
                                <ul class="right">
                                    <li><a href="#">Login</a></li>
                                    <li><a href="#">Signup</a></li>
                                </ul>
                            </section>
                        </nav>
                    </div>
                </div>
            </div>

            @yield('header')
        </header>

        <main class="@yield('main-class')">
            @include('flash::message')

            @yield('content')
        </main>

        @yield('js')
    </body>
</html>
