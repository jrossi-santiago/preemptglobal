/*
 * Preempt Global — centralized analytics loader
 *
 * This is the ONE file that controls tracking site-wide. It is included on
 * every page (the root pages, blog/template.html, and blog/index_template.html),
 * so any change made here — swapping IDs, adding a new tool, removing one —
 * takes effect everywhere the next time pages load. New blog posts inherit
 * this automatically because they're generated from blog/template.html by
 * blog/build.py; you never need to touch individual post files.
 *
 * Setup: replace the two placeholder values below with your real IDs.
 * Until you do, this script intentionally does nothing (no network calls),
 * so it's safe to have deployed before you've created your accounts.
 */
(function () {
  var GA_MEASUREMENT_ID = "G-TD21TYC3BM";        // Google Analytics 4 "Measurement ID", from GA4 Admin > Data Streams
  var POSTHOG_API_KEY    = "phc_oSnhALmdadUFghdFYrRzs7rphWRMzUdqBHcJ4WHG7CLN"; // PostHog "Project API Key", from PostHog Project Settings
  var POSTHOG_HOST       = "https://us.i.posthog.com"; // use https://eu.i.posthog.com if your PostHog project is EU-hosted

  var isPlaceholder = function (value) { return !value || value.indexOf("XXXX") !== -1; };

  // ---- Google Analytics (GA4) ----
  if (!isPlaceholder(GA_MEASUREMENT_ID)) {
    var gaScript = document.createElement("script");
    gaScript.async = true;
    gaScript.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_MEASUREMENT_ID;
    document.head.appendChild(gaScript);

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_MEASUREMENT_ID);
  }

  // ---- PostHog ----
  if (!isPlaceholder(POSTHOG_API_KEY)) {
    var phScript = document.createElement("script");
    phScript.async = true;
    phScript.src = POSTHOG_HOST.replace(".i.posthog.com", "-assets.i.posthog.com") + "/static/array.js";
    phScript.onload = function () {
      window.posthog.init(POSTHOG_API_KEY, {
        api_host: POSTHOG_HOST,
        person_profiles: "identified_only"
      });
    };
    document.head.appendChild(phScript);
  }
})();
