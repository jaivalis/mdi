<!DOCTYPE html>
<html class="no-js" lang="el-GR">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>
            {{ trim($__env->yieldContent('title')) ? $__env->yieldContent('title').' - ' : '' }}Tsepeto
        </title>

        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        {{ HTML::style('components/ionicons/css/ionicons.min.css') }}
        {{ HTML::style('components/fancybox/source/jquery.fancybox.css') }}
        @yield('css')
        {{ HTML::style('css/screen.css') }}

        {{ HTML::script('components/foundation/js/vendor/modernizr.js') }}
    </head>
    <body class="@yield('body-class')">
        <header class="@yield('header-class')">
            <div class="contain-to-grid">
                <div class="row">
                    <div class="large-12 column">
                        <nav class="top-bar" data-topbar>
                            <ul class="title-area">
                                <li class="name">
                                    <h1>
                                        <a href="{{ route('home') }}"><img src="{{ asset('images/ui/logo.png') }}" alt=""></a>
                                    </h1>
                                </li>

                                <li class="toggle-topbar menu-icon">
                                    <a href="#"><span>ΜΕΝΟΥ</span></a>
                                </li>
                            </ul>

                            <section class="top-bar-section">
                                <ul class="right">
                                    <li>Login</li>
                                    <li>Signup</li>
                                </ul>
                            </section>
                        </nav>
                    </div>
                </div>
            </div>

            @yield('header')
        </header>

        <main class="@yield('main-class')">
            <section id="outdated" class="container flash-message" style="display: none">
                <div class="danger">
                    <div class="row">
                        <div class="small-12 column">
                            Ο περιηγητής που χρησιμοποιείται δεν υποστηρίζεται. Παρακαλούμε <a href="http://outdatedbrowser.com/" target="_blank">κάντε αναβάθμιση</a> για να μπορείται να δείτε σωστά το site μας.
                        </div>
                    </div>
                </div>
            </section>
            @include('flash::message')

            @yield('content')
        </main>

        <footer>
            <div class="row bottom-spacer--small text-center">
                <div class="large-12 column">
                    <a href="{{ route('pages.privacy') }}">Δήλωση απορρήτου</a>
                    <a href="{{ route('pages.terms') }}">Όροι χρήσης</a>
                    <a href="http://www.facebook.com">Facebook</a>
                    <a href="http://www.twitter.com">Twitter</a>
                    <a href="{{ route('pages.support') }}">Επικοινωνία</a>
                </div>
            </div>

            <div class="row text-center">
                <div class="large-12 column">
                    &copy; {{ date('Y') }} tsepeto.gr
                </div>
            </div>
        </footer>

        {{ HTML::script('js/app.js') }}
        @yield('js')
    </body>
</html>
