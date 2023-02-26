<template>
  <div id="app">
    <HeaderSection />
    <HeroSection />
    <StatsSection />
    <ServicesSection />
    <AppointmentSection />
    <TestimonialsSection />
    <TeamSection />
    <FaqSection />
    <DepartmentSection />
    <BlogSection />
    <NewsletterSection />
    <FooterSection />
  </div>
</template>

<script>
import HeaderSection from './components/HeaderSection.vue'
import HeroSection from './components/HeroSection.vue'
import StatsSection from './components/StatsSection.vue'
import ServicesSection from './components/ServicesSection.vue'
import AppointmentSection from './components/AppointmentSection.vue'
import TestimonialsSection from './components/TestimonialsSection.vue'
import TeamSection from './components/TeamSection.vue'
import FaqSection from './components/FaqSection.vue'
import DepartmentSection from './components/DepartmentSection.vue'
import BlogSection from './components/BlogSection.vue'
import NewsletterSection from './components/NewsletterSection.vue'
import FooterSection from './components/FooterSection.vue'


export default {
  components: {
    HeaderSection,
    HeroSection,
    StatsSection,
    ServicesSection,
    AppointmentSection,
    TestimonialsSection,
    TeamSection,
    FaqSection,
    DepartmentSection,
    BlogSection,
    NewsletterSection,
    FooterSection
  }
}
</script>

<style>
@import './assets/css/styles.css';
@import './assets/css/swiper-bundle.min.css';
</style>
