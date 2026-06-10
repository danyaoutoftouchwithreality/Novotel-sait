# -*- coding: utf-8 -*-
"""Генератор многостраничного сайта НОВАТЕЛ из единого источника.
Все страницы получают одинаковые шапку/подвал/навигацию и плавные переходы."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Главная"),
    ("8800.html", "Номера 8-800"),
    ("vozmozhnosti.html", "Возможности"),
    ("tarify.html", "Тарифы"),
    ("voprosy.html", "Вопросы"),
    ("kontakty.html", "Контакты"),
]

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')


def head(prefix, title, desc):
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap&subset=cyrillic,cyrillic-ext,latin" rel="stylesheet">
<link rel="icon" href="{prefix}assets/img/mark.png" type="image/png">
<link rel="stylesheet" href="{prefix}assets/css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Перейти к содержимому</a>'''


def nav(prefix, active):
    links = ""
    mobile = ""
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        links += f'\n      <a href="{prefix}{href}"{cls}>{label}</a>'
        mcls = ' class="active"' if href == active else ''
        mobile += f'\n  <a href="{prefix}{href}"{mcls}>{label}</a>'
    return f'''
<header class="nav">
  <div class="container">
    <a class="brand" href="{prefix}index.html" aria-label="НОВАТЕЛ — стабильная альтернатива">
      <img class="brand-logo" src="{prefix}assets/img/logo.png" alt="НОВАТЕЛ — стабильная альтернатива" width="196" height="88">
    </a>
    <nav class="nav-links" aria-label="Основная навигация">{links}
    </nav>
    <div class="nav-cta">
      <div class="nav-phone">8 (800) 775-12-87<span>звонок бесплатный</span></div>
      <a class="btn btn-primary" href="{prefix}kontakty.html">Связаться {ARROW}</a>
      <button class="burger" aria-label="Меню" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu">{mobile}
  <div class="phones">8 (495) 775-12-87 · 8 (800) 775-12-87</div>
</div>
'''


def footer(prefix):
    return f'''
<footer class="footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <a class="brand" href="{prefix}index.html">
          <img class="brand-mark" src="{prefix}assets/img/mark.png" alt="" width="66" height="48">
          <span class="brand-word"><span class="brand-name">НОВАТЕЛ</span><span class="brand-tag">стабильная альтернатива</span></span>
        </a>
        <p class="footer-about">Телекоммуникационная компания. 29 лет помогаем клиентам — крупному и малому бизнесу, индивидуальным предпринимателям.</p>
      </div>
      <div class="footer-col">
        <h5>Возможности</h5>
        <a href="{prefix}8800.html">Номер 8-800</a>
        <a href="{prefix}services/voip.html">IP-телефония</a>
        <a href="{prefix}services/virtual.html">Виртуальный номер</a>
        <a href="{prefix}services/telephonization.html">Телефонизация</a>
        <a href="{prefix}services/long-distance.html">Междугородная и международная связь</a>
      </div>
      <div class="footer-col">
        <h5>Ещё</h5>
        <a href="{prefix}services/teleconference.html">Телеконференции</a>
        <a href="{prefix}services/hosting.html">Хостинг</a>
        <a href="{prefix}services/it-outsourcing.html">ИТ-аутсорсинг</a>
        <a href="{prefix}tarify.html">Тарифы</a>
        <a href="{prefix}voprosy.html">Вопросы</a>
      </div>
      <div class="footer-col">
        <h5>Контакты</h5>
        <a href="tel:+74957751287">8 (495) 775-12-87</a>
        <a href="tel:+78007751287">8 (800) 775-12-87</a>
        <a href="mailto:info@novatel.ru">info@novatel.ru</a>
        <span>129626, г. Москва,<br>ул. Староалексеевская, д. 5, оф. 363</span>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© ООО «НОВАТЕЛ», 1997 – 2026. Все права сохранены законом.<br>Информация на сайте не является публичной офертой.</p>
      <div class="pay-row"><span class="chip">Visa</span><span class="chip">Mastercard</span><span class="chip">МИР</span></div>
    </div>
  </div>
</footer>

<script src="{prefix}assets/js/main.js"></script>
</body>
</html>
'''


def render(filename, prefix, active, title, desc, body):
    html = head(prefix, title, desc) + nav(prefix, active) + '\n<main id="main">\n' + body + '\n</main>\n' + footer(prefix)
    path = os.path.join(BASE, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(filename) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# ============================================================
#  Иконки услуг
# ============================================================
IC = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
 "wifi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 20v-6M2 12a10 10 0 0 1 20 0"/><path d="M5 15a7 7 0 0 1 14 0"/><circle cx="12" cy="19" r="1.5" fill="currentColor" stroke="none"/></svg>',
 "id": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 9h18M8 4v5"/></svg>',
 "lines": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h10"/></svg>',
 "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18Z"/></svg>',
 "office": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 21h18M5 21V7l7-4 7 4v14M9 9h2M9 13h2M13 9h2M13 13h2"/></svg>',
 "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M3 19a6 6 0 0 1 12 0M14 19a5 5 0 0 1 7-4"/></svg>',
 "server": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6l-8-4Z"/><path d="m9 12 2 2 4-4"/></svg>',
}


def service_card(href, icon, title, text, cls="card"):
    return f'''      <article class="{cls}" data-reveal>
        <div class="ico">{IC[icon]}</div>
        <h3>{title}</h3>
        <p>{text}</p>
        <div class="more"><a class="link-arrow" href="{href}">Подробнее {ARROW}</a></div>
      </article>'''


SERVICES = [
 ("8800.html", "phone", "Номер 8-800", "Возможность стать ближе к клиентам, которые могут позвонить вам бесплатно. Подключение и обслуживание 800-х номеров — одна из наших специализаций с 2005 года."),
 ("services/voip.html", "wifi", "IP-телефония", "Сегодня вряд ли кого-то удивишь IP-телефонией. Нас отличает то, что мы ГАРАНТИРУЕМ качественную связь — при условии «нормального» Интернет-канала."),
 ("services/virtual.html", "id", "Виртуальный и многоканальный номер", "Объедините несколько номеров в один и принимайте несколько звонков одновременно — без гудка «занято»."),
 ("services/long-distance.html", "globe", "Междугородная и международная связь", "Альтернативная связь на существующих линиях по ПИН-коду и телефонным картам. Международной связью мы специализируемся с 1994 года."),
 ("services/telephonization.html", "office", "Телефонизация офиса", "Комплексная телефонизация: цифровые каналы, городские номера и линии, объединение офисов и складов, замена АТС, подключение по ВОЛС."),
 ("services/teleconference.html", "people", "Телеконференции", "Одновременное удалённое общение от 2 до 60 человек в разных частях города, страны или мира."),
 ("services/hosting.html", "server", "Хостинг", "Круглосуточный доступ к сайту по высокоскоростным каналам. Как оператор связи мы располагаем избыточной пропускной способностью."),
 ("services/it-outsourcing.html", "shield", "ИТ-аутсорсинг", "Обеспечение бесперебойной работы офисов по принципу «ВСЁ ВКЛЮЧЕНО!» — силами компании «Стабилити Системс»."),
]


def subnav(prefix, crumb, parent=None):
    mid = ""
    if parent:
        mid = f'<a href="{prefix}{parent[0]}">{parent[1]}</a><span class="sep">/</span>'
    return (f'<div class="subnav" data-reveal><a href="{prefix}index.html">Главная</a>'
            f'<span class="sep">/</span>{mid}<span class="{ "" }">{crumb}</span></div>')


def page_header(prefix, crumb, eyebrow, title, lead, parent=None):
    return f'''<section class="page-hero">
  <div class="container">
    {subnav(prefix, crumb, parent)}
    <span class="eyebrow" data-reveal>{eyebrow}</span>
    <h1 data-reveal data-delay="1">{title}</h1>
    <p class="lead" data-reveal data-delay="2">{lead}</p>
  </div>
</section>'''


def buttons_block(prefix):
    return f'''    <div style="margin-top:2.4em;display:flex;gap:14px;flex-wrap:wrap">
      <a class="btn btn-primary btn-lg" href="{prefix}kontakty.html">Оставить заявку {ARROW}</a>
      <a class="btn btn-ghost btn-lg" href="{prefix}tarify.html">Тарифы</a>
    </div>'''


def cta_block(prefix):
    return f'''    <div class="callout" style="margin-top:2.6em">
      <p>Остались вопросы? Позвоните нам по номеру <strong>8 800 775 12 87</strong> или <a href="mailto:info@novatel.ru">напишите</a> — подскажем оптимальный вариант подключения и использования.</p>
    </div>
{buttons_block(prefix)}'''


def bento(prefix):
    """Сетка из 8 услуг (используется на главной и в «Возможностях»)."""
    L = lambda p: f"{prefix}{p}"
    return f'''    <div class="bento">
      <article class="card card--feature" data-reveal>
        <div class="ico">{IC['phone']}</div>
        <h3>Телефонный номер 8-800</h3>
        <p>Возможность стать ближе к своим клиентам и партнёрам по бизнесу, которые могут позвонить вам бесплатно. Как известно, «скупой платит дважды», а в условиях современного бизнеса скупость может стоить ещё дороже. Не будьте скупыми — будьте ближе!</p>
        <div class="more"><a class="link-arrow" href="{L('8800.html')}">Подробнее об услуге {ARROW}</a></div>
      </article>
      <article class="card col-2" data-reveal data-delay="1">
        <div class="ico">{IC['wifi']}</div>
        <h3>IP-телефония</h3>
        <p>Сегодня вряд ли кого-то удивишь IP-телефонией. Нас отличает то, что мы ГАРАНТИРУЕМ своим клиентам качественную связь, при условии что у них «нормальный» Интернет-канал.</p>
        <div class="more"><a class="link-arrow" href="{L('services/voip.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-3" data-reveal>
        <div class="ico">{IC['id']}</div>
        <h3>Виртуальный телефонный номер</h3>
        <p>Возможность объединить несколько разных телефонных номеров, как городских, так и мобильных, единым телефонным номером и повысить эффективность своей рекламы. Сделайте так, чтобы до вас можно было легко дозвониться.</p>
        <div class="more"><a class="link-arrow" href="{L('services/virtual.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-3" data-reveal data-delay="1">
        <div class="ico">{IC['lines']}</div>
        <h3>Многоканальный номер</h3>
        <p>Возможность одновременно принимать и делать самим несколько телефонных звонков. Это способ избежать гудка «занято» в телефонной линии всякий раз, когда вам нужно принять очередной звонок клиента.</p>
        <div class="more"><a class="link-arrow" href="{L('services/virtual.html')}#multi">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-3" data-reveal>
        <div class="ico">{IC['globe']}</div>
        <h3>Междугородная и международная связь</h3>
        <p>«НОВАТЕЛ» — один из родоначальников рынка альтернативной междугородной связи на существующих линиях с помощью ПИН-кода и по телефонным картам. Международной связью мы специализируемся с 1994 года.</p>
        <div class="more"><a class="link-arrow" href="{L('services/long-distance.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-3" data-reveal data-delay="1">
        <div class="ico">{IC['office']}</div>
        <h3>Телефонизация офиса и предприятий</h3>
        <p>Комплексная телефонизация офиса: цифровые каналы, городские номера и дополнительные линии, выделенный доступ в Интернет, объединение нескольких офисов и складов, включая региональные. Одно из приоритетных для нас направлений.</p>
        <div class="more"><a class="link-arrow" href="{L('services/telephonization.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-2" data-reveal>
        <div class="ico">{IC['people']}</div>
        <h3>Телеконференции</h3>
        <p>Одновременное удалённое общение от 2 до 60 человек в разных частях города, страны или мира.</p>
        <div class="more"><a class="link-arrow" href="{L('services/teleconference.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-2" data-reveal data-delay="1">
        <div class="ico">{IC['server']}</div>
        <h3>Хостинг</h3>
        <p>Круглосуточный бесперебойный доступ к веб-сайту по высокоскоростным каналам связи. Как оператор связи мы располагаем избыточной пропускной способностью.</p>
        <div class="more"><a class="link-arrow" href="{L('services/hosting.html')}">Подробнее {ARROW}</a></div>
      </article>
      <article class="card col-2" data-reveal data-delay="2">
        <div class="ico">{IC['shield']}</div>
        <h3>ИТ-аутсорсинг</h3>
        <p>Обеспечение бесперебойной работы офисов по принципу «ВСЁ ВКЛЮЧЕНО!» — силами компании «Стабилити Системс».</p>
        <div class="more"><a class="link-arrow" href="{L('services/it-outsourcing.html')}">Подробнее {ARROW}</a></div>
      </article>
    </div>'''


# ============================================================
#  ГЛАВНАЯ
# ============================================================
def home_body():
    return f'''<section class="hero">
  <div class="hero-bg">
    <div class="hero-grid-lines"></div>
    <svg class="hero-motif" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <circle cx="70" cy="58" r="38" fill="#4F7A57" opacity=".9"/>
      <circle cx="132" cy="52" r="27" fill="#6E9A74" opacity=".85"/>
      <circle cx="140" cy="112" r="32" fill="#4F7A57" opacity=".9"/>
      <circle cx="84" cy="120" r="25" fill="#1F4E8C" opacity=".9"/>
      <circle cx="116" cy="84" r="21" fill="#163A6B" opacity=".95"/>
      <circle cx="52" cy="106" r="16" fill="#8FB6DA" opacity=".85"/>
    </svg>
  </div>
  <div class="container hero-inner">
    <span class="pill" data-reveal><span class="dot"></span>Телекоммуникационная компания · с 1997 года</span>
    <h1 class="display" data-reveal data-delay="1">Стабильная<br><span class="grad">альтернатива</span> связи</h1>
    <p class="lead" data-reveal data-delay="2">29 лет помогаем клиентам. Номера 8-800, IP-телефония, виртуальные и многоканальные номера, телефонизация офисов, междугородная и международная связь — для крупного и малого бизнеса.</p>
    <div class="hero-actions" data-reveal data-delay="3">
      <a class="btn btn-primary btn-lg" href="vozmozhnosti.html">Смотреть возможности {ARROW}</a>
      <a class="btn btn-ghost btn-lg" href="kontakty.html">Получить консультацию</a>
    </div>
    <div class="hero-trust" data-reveal data-delay="4">
      <div class="t"><span class="num">29</span><span class="lbl">лет на рынке связи</span></div>
      <span class="sep"></span>
      <div class="t"><span class="num">1997</span><span class="lbl">год основания</span></div>
      <span class="sep"></span>
      <div class="t"><span class="num">№1</span><span class="lbl">во многих решениях</span></div>
    </div>
  </div>
</section>

<section class="partners">
  <div class="container">
    <p class="partners-label" data-reveal>Работаем с ведущими операторами и производителями</p>
    <div class="partners-row" data-reveal data-delay="1">
      <span>Ростелеком</span><span>МТТ</span><span>МТС</span><span>MGTS</span><span>Билайн</span><span>Мегафон</span><span>Asterisk</span><span>Cisco</span><span>Panasonic</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Возможности</span>
      <h2 class="h2" style="margin-top:16px">Связь, на которую можно положиться</h2>
      <p class="lead">Полный спектр телекоммуникационных решений для бизнеса — от бесплатного номера 8-800 до комплексной телефонизации офиса и ИТ-аутсорсинга.</p>
    </div>
{bento("")}
    <div style="margin-top:32px" data-reveal><a class="btn btn-ghost btn-lg" href="vozmozhnosti.html">Все возможности {ARROW}</a></div>
  </div>
</section>

<section class="section--tight stats-band">
  <div class="container">
    <div class="stats-grid">
      <div class="stat" data-reveal><div class="n"><span data-count="29">29</span></div><div class="l">года помогаем клиентам</div></div>
      <div class="stat" data-reveal data-delay="1"><div class="n">1997</div><div class="l">год основания компании</div></div>
      <div class="stat" data-reveal data-delay="2"><div class="n">8&nbsp;800</div><div class="l">бесплатные номера с 2005 года</div></div>
      <div class="stat" data-reveal data-delay="3"><div class="n"><span data-count="13">13</span></div><div class="l">отраслевых решений, где мы были первыми</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div data-reveal>
      <span class="eyebrow">О компании</span>
      <h2 class="h2" style="margin-top:16px">Вместо тысячи слов</h2>
      <p class="lead" style="margin-top:18px">Если вам раньше не доводилось ничего слышать о нашей — в какой-то мере легендарной компании — то это вовсе не означает, что нас не существовало.</p>
      <ul class="feature-list">
        <li><span class="fi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg></span><div><h4>Реагируем, а не создаём видимость</h4><p>Мы не создаём видимость своей идеальности, а оперативно реагируем на обращения клиентов и устраняем возникающие проблемы.</p></div></li>
        <li><span class="fi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"/></svg></span><div><h4>Проверенное оборудование</h4><p>Asterisk, Cisco, Panasonic и другие производители — техника и ПО, проверенные годами эксплуатации.</p></div></li>
        <li><span class="fi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span><div><h4>Уважаемые партнёры</h4><p>Сотрудничаем с Ростелеком, МТТ, МТС, MGTS, Билайн и Мегафон.</p></div></li>
      </ul>
    </div>
    <aside class="glass-panel" data-reveal data-delay="1">
      <span class="quote-mark">“</span>
      <p class="quote">Не верьте нашим словам — поверьте нашим делам.</p>
      <p class="quote-cite">— НОВАТЕЛ, телекоммуникационная компания с 1997 года</p>
    </aside>
  </div>
</section>

<section class="section" style="background:var(--bg-soft)">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">Новости</span>
      <h2 class="h2" style="margin-top:16px">Главные новости</h2>
    </div>
    <div class="news-grid">
      <article class="news-card" data-reveal><div class="date">24.01.2026</div><h4>«НОВАТЕЛу» уже 29 лет!</h4><p>Жизнь продолжает испытывать нас на прочность.</p></article>
      <article class="news-card" data-reveal data-delay="1"><div class="date">29.12.2025</div><h4>С новым, 2026 годом и Рождеством!</h4><p>Процветания, успехов, мира в новом году!</p></article>
      <article class="news-card" data-reveal data-delay="2"><div class="date">10.11.2025</div><h4>Виртуальная АТС становится платной</h4><p>Исключение составят клиенты, чьи номера подключены напрямую по VoIP-телефонии.</p></article>
      <article class="news-card" data-reveal><div class="date">31.10.2025</div><h4>Маркировка звонков — разрабатывается открытый API</h4><p>Из Минцифры был получен ответ на коллективное обращение операторов связи.</p></article>
      <article class="news-card" data-reveal data-delay="1"><div class="date">30.09.2025</div><h4>Маркировка исходящих звонков и их тарификация</h4><p>Информируем о том, какие данные у нас имеются на текущий момент.</p></article>
      <article class="news-card alert" data-reveal data-delay="2"><div class="date">17.04.2025</div><h4>!! ОСТОРОЖНО — МОШЕННИКИ !!</h4><p>Вам могут позвонить мошенники от имени «НОВАТЕЛ» по поводу переоформления договоров и номеров.</p></article>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="container">
    <div class="cta" data-reveal>
      <span class="eyebrow">Начнём сотрудничество</span>
      <h2 class="h2" style="margin-top:16px">Подскажем оптимальное решение для вашего бизнеса</h2>
      <p>Позвоните нам — мы обязательно ответим на ваши вопросы и предложим оптимальный вариант подключения и использования.</p>
      <div class="cta-phone">8 800 775 12 87</div>
      <div class="cta-actions">
        <a class="btn btn-primary btn-lg" href="kontakty.html">Оставить заявку</a>
        <a class="btn btn-ghost btn-lg" href="tarify.html">Смотреть тарифы</a>
      </div>
    </div>
  </div>
</section>'''


# ============================================================
#  ВОЗМОЖНОСТИ
# ============================================================
def vozmozhnosti_body():
    return f'''{page_header("", "Возможности", "Услуги компании", "Возможности НОВАТЕЛ", "Полный спектр телекоммуникационных решений для бизнеса — от бесплатного номера 8-800 до комплексной телефонизации офиса, междугородной связи и ИТ-аутсорсинга.")}

<section class="section" style="padding-top:24px">
  <div class="container">
{bento("")}
  </div>
</section>

<section class="section--tight stats-band">
  <div class="container">
    <div class="stats-grid">
      <div class="stat" data-reveal><div class="n">29</div><div class="l">лет опыта в связи</div></div>
      <div class="stat" data-reveal data-delay="1"><div class="n">8</div><div class="l">направлений услуг</div></div>
      <div class="stat" data-reveal data-delay="2"><div class="n">1994</div><div class="l">с этого года — международная связь</div></div>
      <div class="stat" data-reveal data-delay="3"><div class="n">2005</div><div class="l">с этого года — номера 8-800</div></div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="container">
    <div class="cta" data-reveal>
      <h2 class="h2" style="margin-top:0">Не знаете, что подойдёт именно вам?</h2>
      <p>Позвоните — подскажем оптимальный вариант под вашу задачу.</p>
      <div class="cta-actions">
        <a class="btn btn-primary btn-lg" href="kontakty.html">Получить консультацию</a>
        <a class="btn btn-ghost btn-lg" href="voprosy.html">Частые вопросы</a>
      </div>
    </div>
  </div>
</section>'''


# ============================================================
#  ТАРИФЫ
# ============================================================
def tarify_body():
    return f'''{page_header("", "Тарифы", "Цены", "Тарифы", "Прозрачные условия по основным услугам. Точные цены на отдельные позиции зависят от конфигурации — уточняйте у нас, мы подберём оптимальный вариант.")}

<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2 class="h2">Номер 8-800</h2>
      <p class="lead">Подключение — 0 ₽. Ежемесячная плата за сам номер — 0 ₽. Ежемесячный платёж состоит из абонентской платы за номер 8-800 и гарантированного (минимального) платежа за звонки.</p>
    </div>
    <div class="price-grid">
      <article class="price-card" data-reveal>
        <div class="plan">Минималка</div>
        <div class="amount">1 500 ₽<small> / мес</small></div>
        <ul class="plist">
          <li>Подключение — 0 ₽</li>
          <li>Абонентская плата за номер — 0 ₽</li>
          <li>Гарантированный минимальный платёж за звонки</li>
        </ul>
        <div class="more"><a class="link-arrow" href="kontakty.html">Подключить {ARROW}</a></div>
      </article>
      <article class="price-card feature" data-reveal data-delay="1">
        <span class="price-badge">Популярный</span>
        <div class="plan">«Золотой»</div>
        <div class="amount">5 000 ₽<small> / мес</small></div>
        <ul class="plist">
          <li>Расширенный пакет включённых минут</li>
          <li>Подключение — 0 ₽</li>
          <li>Оптимально для активного входящего потока</li>
        </ul>
        <div class="more"><a class="link-arrow" href="kontakty.html">Подключить {ARROW}</a></div>
      </article>
      <article class="price-card" data-reveal data-delay="2">
        <div class="plan">Безлимит</div>
        <div class="amount">Индивидуально</div>
        <ul class="plist">
          <li>Полный безлимит</li>
          <li>Условный безлимит</li>
          <li>Рассчитываем под ваш объём звонков</li>
        </ul>
        <div class="more"><a class="link-arrow" href="kontakty.html">Запросить расчёт {ARROW}</a></div>
      </article>
    </div>
    <p class="price-note" data-reveal>Точные цены на конкретные серии 800-х номеров запрашивайте у нас отдельно — стоимость зависит от серии и категории номера (чем «ниже» категория, тем номер дороже).</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container split">
    <div data-reveal>
      <h2 class="h2">Многоканальный телефон</h2>
      <p class="lead" style="margin-top:16px">Городской номер, по которому одновременно может идти несколько телефонных разговоров. Типовые подключения — 2-х, 4-х, 8-ми, 16-ти и 32-х канальные номера.</p>
      <ul class="feature-list">
        <li><span class="fi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg></span><div><h4>На оборудовании НОВАТЕЛ</h4><p>Платы за оборудование нет.</p></div></li>
        <li><span class="fi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg></span><div><h4>На своём оборудовании (АТС / IP-шлюз)</h4><p>Оплата только за подключение, дополнительные линии — бесплатно.</p></div></li>
      </ul>
    </div>
    <aside class="price-card feature" data-reveal data-delay="1" style="max-width:380px">
      <div class="plan">10 линий</div>
      <div class="amount">2 500 ₽</div>
      <ul class="plist">
        <li>Одновременный приём нескольких звонков</li>
        <li>Без гудка «занято»</li>
        <li>Масштабирование до 32 каналов</li>
      </ul>
      <div class="more"><a class="link-arrow" href="kontakty.html">Подключить {ARROW}</a></div>
    </aside>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head" data-reveal>
      <h2 class="h2">Хостинг</h2>
      <p class="lead">Цены указаны без учёта НДС. Оплата услуг производится минимум за 12 месяцев (в редких случаях возможна оплата за 6 месяцев).</p>
    </div>
    <div class="split" style="align-items:start">
      <div data-reveal>
        <h3 class="h3" style="margin-bottom:14px">Для хостинга</h3>
        <table class="data-table">
          <thead><tr><th>Тариф</th><th>Объём</th><th>В год</th></tr></thead>
          <tbody>
            <tr><td>Базовый</td><td>5 Гб</td><td>2 500 ₽</td></tr>
            <tr><td>Стандартный</td><td>10 Гб</td><td>5 000 ₽</td></tr>
            <tr><td>Оптимальный</td><td>15 Гб</td><td>10 000 ₽</td></tr>
          </tbody>
        </table>
      </div>
      <div data-reveal data-delay="1">
        <h3 class="h3" style="margin-bottom:14px">Для клиентов телеком-услуг<br><small style="font-weight:500;color:var(--text-soft);font-size:.9rem">при ежемесячном объёме услуг от 2 500 ₽</small></h3>
        <table class="data-table">
          <thead><tr><th>Тариф</th><th>Объём</th><th>В год</th></tr></thead>
          <tbody>
            <tr><td>Базовый</td><td>5 Гб</td><td>бесплатно</td></tr>
            <tr><td>Стандартный</td><td>10 Гб</td><td>бесплатно</td></tr>
            <tr><td>Оптимальный</td><td>15 Гб</td><td>бесплатно</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <p class="price-note" data-reveal>В тариф входит: домены на площадке (5 / 10 / 15), базы данных MySQL, интернет-трафик без ограничений, почтовые ящики, внешний IP-адрес — бесплатно.</p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="glass-panel" data-reveal>
      <h2 class="h3" style="margin-bottom:10px">Московские номера, телеконференции и индивидуальные решения</h2>
      <p style="color:var(--text-soft)">Красивые номера, номера на выбор, пары номеров, телефон в офис и виртуальные номера, а также телеконференции рассчитываются индивидуально — жёсткого прайс-листа на эти услуги нет. Позвоните <strong style="color:var(--ink)">8&nbsp;800&nbsp;775&nbsp;12&nbsp;87</strong>, и мы подберём оптимальный вариант под вашу задачу.</p>
      <div style="margin-top:22px;display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn btn-primary btn-lg" href="kontakty.html">Запросить расчёт {ARROW}</a>
        <a class="btn btn-ghost btn-lg" href="vozmozhnosti.html">Все возможности</a>
      </div>
    </div>
  </div>
</section>'''


# ============================================================
#  ВОПРОСЫ
# ============================================================
def faq_item(q, a):
    plus = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
    return f'''      <details data-reveal>
        <summary>{q}{plus}</summary>
        <div class="ans">{a}</div>
      </details>'''


def voprosy_body():
    faqs = [
        ("Что такое номер 8-800 и зачем он нужен?",
         "<p>Это возможность стать ближе к своим клиентам, которые могут позвонить вам <strong>бесплатно</strong>. Бесплатными такие номера являются только для тех, кто на них звонит — за все звонки, поступившие на 800-й номер, платит его пользователь.</p>"),
        ("Кому нужен номер 8-800?",
         "<p>Он необходим, если вы по роду деятельности работаете с регионами России или ваши клиенты могут звонить с мобильных телефонов. Крупным корпорациям такой номер нужен и для имиджа, но малому бизнесу и ИП он может быть нужен ещё больше — чтобы клиент позвонил сразу, как только увидел вашу рекламу.</p>"),
        ("Сколько в среднем стоит обслуживание номера 8-800?",
         "<p>По нашему опыту, разброс средних расходов большинства клиентов, пользующихся номерами 8-800, не превышает <strong>3–5 тыс. руб. в месяц</strong>. Точные цены на конкретные серии и категории номеров запрашивайте у нас отдельно.</p>"),
        ("Гарантируете ли вы качество IP-телефонии?",
         "<p>Да — мы <strong>ГАРАНТИРУЕМ</strong> своим клиентам качественную связь по IP-телефонии при условии, что у них «нормальный» Интернет-канал. Качество зависит не только от VoIP-оборудования, но и от стабильности всего маршрута интернет-канала.</p>"),
        ("Что такое виртуальный, единый и интеллектуальный номер?",
         "<p><strong>Виртуальный</strong> — несуществующий, но возможный. <strong>Единый</strong> — один, общий, объединённый номер. <strong>Интеллектуальный</strong> — думающий, производящий анализ данных по заложенным программам. Услуга объединяет несколько телефонных номеров в один и обрабатывает звонки централизованно.</p>"),
        ("Что такое многоканальный номер?",
         "<p>Это возможность одновременно принимать и делать самим несколько телефонных звонков — способ избежать гудка «занято» всякий раз, когда нужно принять очередной звонок клиента.</p>"),
        ("Сколько лет компании?",
         "<p>29 лет. «НОВАТЕЛ» работает на телекоммуникационном рынке России с января 1997 года и является одним из самых стабильных и надёжных малых операторов связи России.</p>"),
        ("Как с вами связаться?",
         "<p>Позвоните по номеру <strong>8 800 775-12-87</strong> (звонок бесплатный) или напишите на <a href=\"mailto:info@novatel.ru\">info@novatel.ru</a>. Можно также оставить заявку на странице <a href=\"kontakty.html\">Контакты</a>.</p>"),
    ]
    faq_html = "\n".join(faq_item(q, a) for q, a in faqs)
    return f'''{page_header("", "Вопросы", "Помощь", "Вопросы и ответы", "Кто бы вы ни были — мы найдём общий язык. Выберите, что ближе вам, и найдите ответы на частые вопросы о наших услугах.")}

<section class="section" style="padding-top:24px;background:var(--bg-soft)">
  <div class="container">
    <div class="section-head" data-reveal>
      <span class="eyebrow">С чего начать</span>
      <h2 class="h2" style="margin-top:16px">Выберите свой путь</h2>
    </div>
    <div class="paths">
      <article class="path-card" data-reveal>
        <div class="num">01</div><div class="who">Новичкам</div>
        <div class="head">Приятно познакомиться!</div>
        <p>«НОВАТЕЛ» — один из самых стабильных и надёжных малых операторов связи России, работающий на рынке с января 1997 года. С нами уже много лет сотрудничают самые крупные операторы связи России. Вы ничем не рискуете, начиная своё сотрудничество с нами!</p>
        <div class="more"><a class="link-arrow" href="kontakty.html">Начать сотрудничество {ARROW}</a></div>
      </article>
      <article class="path-card" data-reveal data-delay="1">
        <div class="num">02</div><div class="who">Бывалым</div>
        <div class="head">Здравый взгляд на знакомые вещи</div>
        <p>Чтобы оценить что-либо, это что-либо нужно проверить на деле. У операторов однотипное оборудование и одни и те же поставщики, а качество никогда не стоило и не будет стоить дёшево. Нас отличают порядочность, открытость и искренность, которыми никто из конкурентов похвастаться не сможет.</p>
        <div class="more"><a class="link-arrow" href="kontakty.html">Проверить на деле {ARROW}</a></div>
      </article>
      <article class="path-card" data-reveal data-delay="2">
        <div class="num">03</div><div class="who">Сомневающимся</div>
        <div class="head">Единственный способ поверить — проверить</div>
        <p>Сомнение всегда есть там, где нет полной уверенности в чём-либо. Мы с честью прошли испытание экономическим кризисом в августе 1998 года и не покупаем репутацию низкими тарифами. Протестируйте услуги сразу у нескольких поставщиков — если среди них будет «НОВАТЕЛ», вы вряд ли проиграете.</p>
        <div class="more"><a class="link-arrow" href="kontakty.html">Убедиться самим {ARROW}</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" data-reveal>
      <span class="eyebrow">FAQ</span>
      <h2 class="h2" style="margin-top:16px">Частые вопросы</h2>
    </div>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>'''


# ============================================================
#  КОНТАКТЫ
# ============================================================
def kontakty_body():
    return f'''{page_header("", "Контакты", "Связь с нами", "Контакты", "Оставьте заявку — мы перезвоним, ответим на вопросы и предложим оптимальный вариант подключения. Или свяжитесь с нами любым удобным способом.")}

<section class="section" style="padding-top:24px">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card" data-reveal>
        <div class="ci">{IC['phone']}</div>
        <div class="lbl">Телефоны</div>
        <div class="val"><a href="tel:+74957751287">8 (495) 775-12-87</a></div>
        <div class="val"><a href="tel:+78007751287">8 (800) 775-12-87</a></div>
        <div class="sub">Факс: (495) 775-12-88</div>
      </div>
      <div class="contact-card" data-reveal data-delay="1">
        <div class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></div>
        <div class="lbl">Электронная почта</div>
        <div class="val"><a href="mailto:info@novatel.ru">info@novatel.ru</a></div>
        <div class="sub">Ответим на любые вопросы по услугам</div>
      </div>
      <div class="contact-card" data-reveal data-delay="2">
        <div class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>
        <div class="lbl">Адрес</div>
        <div class="val" style="font-size:1.02rem">129626, г. Москва, ул. Староалексеевская, дом 5, офис 363</div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="consult" style="padding-top:0">
  <div class="container consult">
    <div class="consult-aside" data-reveal>
      <span class="eyebrow">Получить консультацию</span>
      <h2 class="h2" style="margin-top:16px">Оставьте заявку</h2>
      <p class="lead" style="margin-top:18px">Мы перезвоним, ответим на вопросы и предложим оптимальный вариант подключения. Или позвоните прямо сейчас: <strong style="color:var(--ink)">8&nbsp;800&nbsp;775&nbsp;12&nbsp;87</strong>.</p>
      <ul class="reassure">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>Реагируем оперативно — не создаём видимость идеальности.</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>29 лет на рынке связи, с нами сотрудничают крупнейшие операторы.</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>Вы ничем не рискуете, начиная сотрудничество с нами.</li>
      </ul>
    </div>
    <div class="form-card" data-reveal data-delay="1">
      <form id="lead-form" novalidate>
        <div class="form-row">
          <div class="field"><label for="lf-name">Имя <span class="req">*</span></label><input id="lf-name" name="name" type="text" placeholder="Как к вам обращаться" required autocomplete="name"></div>
          <div class="field"><label for="lf-phone">Телефон <span class="req">*</span></label><input id="lf-phone" name="phone" type="tel" placeholder="+7 (___) ___-__-__" required autocomplete="tel"></div>
        </div>
        <div class="field"><label for="lf-email">E-mail</label><input id="lf-email" name="email" type="email" placeholder="you@company.ru" autocomplete="email"></div>
        <div class="field"><label for="lf-service">Интересующая услуга</label>
          <select id="lf-service" name="service">
            <option value="">Выберите услугу…</option>
            <option>Номер 8-800</option><option>IP-телефония</option><option>Виртуальный / многоканальный номер</option>
            <option>Междугородная и международная связь</option><option>Телефонизация офиса</option>
            <option>Телеконференции</option><option>Хостинг</option><option>ИТ-аутсорсинг</option><option>Другое / не определился</option>
          </select>
        </div>
        <div class="field"><label for="lf-msg">Сообщение</label><textarea id="lf-msg" name="message" placeholder="Коротко опишите вашу задачу"></textarea></div>
        <button class="btn btn-primary btn-lg" type="submit">Отправить заявку {ARROW}</button>
        <p class="form-status" id="lf-status" role="status"></p>
        <p class="form-note">Нажимая «Отправить заявку», вы соглашаетесь на обработку персональных данных. Информация на сайте не является публичной офертой.</p>
      </form>
    </div>
  </div>
</section>'''


# ============================================================
#  ДЕТАЛЬНЫЕ СТРАНИЦЫ УСЛУГ
# ============================================================
def service_page(prefix, crumb, eyebrow, title, lead, prose, cta="full"):
    tail = cta_block(prefix) if cta == "full" else buttons_block(prefix)
    return f'''{page_header(prefix, crumb, eyebrow, title, lead, parent=("vozmozhnosti.html","Возможности"))}

<section class="section" style="padding-top:24px">
  <div class="container article prose" data-reveal>
{prose}
{tail}
  </div>
</section>'''


SERVICE_PAGES = {
 "services/voip.html": dict(
   crumb="IP-телефония", title="IP-телефония",
   lead="Сегодня вряд ли кого-то удивишь IP-телефонией. Нас отличает то, что мы ГАРАНТИРУЕМ своим клиентам качественную связь — при условии что у них «нормальный» Интернет-канал.",
   desc="IP-телефония от НОВАТЕЛ. Гарантируем качественную связь при нормальном интернет-канале — благодаря отношениям с крупнейшими поставщиками Интернета в Москве.",
   prose='''    <h2>Основные определения</h2>
    <p><strong>VoIP (ВоИП)</strong> — происходит от англ. «Voice over IP» — «голос поверх IP». Это способ передачи голоса через объединённые сети. При этом совсем не обязательно речь идёт об использовании глобального интернета — технология применяется и для внутриорганизационной связи.</p>
    <h2>От чего зависит качество IP-телефонии</h2>
    <p>Качество IP-телефонии зависит не только от того, каким VoIP-оборудованием вы пользуетесь. Не меньшее значение имеет стабильность маршрута интернет-канала. Важны также интернет-провайдер клиента и каналы связи оператора VoIP.</p>
    <h2>Как правильно проверять подключение</h2>
    <p>Практически всегда упускается из виду ещё одна проверка — всей трассы (ТРАССИРОВКА), по которой голос будет ходить. Рекомендуется проверять не только время отклика (PING), но и полный маршрут (TRACEROUTE). Односторонняя проверка может скрыть проблемы в обратном направлении сигнала.</p>
    <h2>Решение НОВАТЕЛ</h2>
    <p>У нас выстроены отношения с крупнейшими поставщиками Интернета в Москве, что гарантирует нашим клиентам высокую надёжность и стабильность передачи голоса.</p>'''),
 "services/virtual.html": dict(
   crumb="Виртуальный номер", title="Виртуальный · Единый · Интеллектуальный номер",
   lead="Возможность объединить несколько разных телефонных номеров, как городских, так и мобильных, единым телефонным номером и повысить эффективность своей рекламы.",
   desc="Виртуальный, единый, интеллектуальный телефонный номер от НОВАТЕЛ. Объединение нескольких номеров в один и многоканальная связь без сигнала «занято».",
   prose='''    <h2>Что это такое</h2>
    <p><strong>Виртуальный</strong> номер — несуществующий, но возможный. <strong>Единый</strong> означает один, общий, объединённый номер. <strong>Интеллектуальный</strong> означает думающий, производящий анализ данных по заложенным программам.</p>
    <p>Услуга объединяет несколько телефонных номеров в один, обрабатывая звонки централизованно. Применяется для компаний с филиалами, при частых переездах, для временных офисов. Сделайте так, чтобы до вас можно было легко дозвониться.</p>
    <h2 id="multi">Многоканальный телефонный номер</h2>
    <p>Возможность одновременно принимать и делать самим несколько телефонных звонков. Это способ избежать гудка «занято» в телефонной линии всякий раз, когда вам нужно принять очередной звонок клиента.</p>'''),
 "services/long-distance.html": dict(
   crumb="Междугородная и международная связь", title="Междугородная и международная связь",
   lead="«НОВАТЕЛ» — один из родоначальников рынка альтернативной междугородной телефонной связи, предоставляемой на существующих телефонных линиях с помощью ПИН-кода и по телефонным картам.",
   desc="Альтернативная междугородная и международная связь от НОВАТЕЛ: по ПИН-коду и телефонным картам, по выделенной линии и волоконно-оптическому кабелю.",
   prose='''    <p>Сегодня междугородняя телефонная связь стремительно дешевеет, тем не менее наша компания идёт в ногу с рынком. Мы знаем, что междугородняя связь может быть дешевле. Вы тоже способны убедиться в этом, если станете нашим клиентом. Международной телефонной связью — звонками по СНГ, странам Балтии и всему остальному миру — мы специализируемся с 1994 года. Мы не сторонники IP-телефонии и предпочитаем традиционные линии связи. Нашими поставщиками междугородной и международной связи являются очень уважаемые и титулованные операторы связи.</p>
    <h2>Лицензия</h2>
    <p>ООО «НОВАТЕЛ» является оператором местной телефонной связи. В соответствии с имеющейся лицензией компания обязана обеспечить своим клиентам доступ к услугам междугородной телефонной связи.</p>
    <h2>Междугородная связь путём авторизации</h2>
    <p>Данный вид услуг универсален тем, что для осуществления междугородных телефонных разговоров не требует смены телефонных линий и номеров. Процесс подключения предусматривает дозвон до номера доступа, ввод ПИН-кода и набор номера абонента по стандартной схеме.</p>
    <h2>Междугородная связь по выделенной линии</h2>
    <p>Рекомендуется при месячном объёме свыше 300 долларов США. С использованием технологии высокочастотного уплотнения мы способны на существующей телефонной линии предоставить вам до 8 дополнительных линий.</p>
    <h2>Междугородная связь по волокну</h2>
    <p>При объёмах, превышающих 1.000 долларов ежемесячно, предлагается волоконно-оптический кабель. ВОЛС гарантирует высокое качество связи и позволяет абоненту не знать проблем с качеством.</p>
    <h2>Телефонные карты</h2>
    <p>Доступны пополняемые карты для тех, кто желает оценить качество или имеет минимальный объём переговоров.</p>'''),
 "services/telephonization.html": dict(
   crumb="Телефонизация", title="Телефонизация офиса и предприятий",
   lead="Телефонизация офисов — одно из приоритетных для нас направлений деятельности. Мы не утверждаем, что можем всё, но эту задачу решаем квалифицированно.",
   desc="Комплексная телефонизация офиса и объекта от НОВАТЕЛ: цифровые каналы, городские номера и линии, объединение офисов, замена АТС, подключение по ВОЛС.",
   prose='''    <h2>Как мы работаем</h2>
    <p>Телефонизация офиса и телефонизация объекта подразумевает, что вы обращаетесь к нам, ставите задачу по телефонизации вашего офиса или объекта — по тому, сколько и каких цифровых каналов требуется организовать, сколько городских номеров и дополнительных линий к ним нужно подключить и т.п., а мы анализируем поставленную задачу и предлагаем вам способы её решения.</p>
    <p>Мы применяем оборудование и программные решения различных международных и отечественных производителей телекоммуникационной техники, причём именно ту технику, которую проверили и которой доверяем за годы работы.</p>
    <h2>Какие задачи решаем</h2>
    <ul class="bullets">
      <li>Комплексная телефонизация офиса с предоставлением услуг телефонной связи (междугородняя и международная связь).</li>
      <li>Телефонные линии и номера, выделенный доступ в Интернет.</li>
      <li>Объединение нескольких офисов, складов и т.п., включая региональные.</li>
      <li>Замена существующей офисной АТС на что-нибудь поновее.</li>
      <li>Подключение по волоконно-оптической линии связи (ВОЛС).</li>
    </ul>
    <p>Стремитесь решить иные задачи, связанные с телефонизацией вашего офиса или предприятия? Ищете оператора связи, способного квалифицированно решить это? Позвоните нам.</p>
    <h2>Новые телефонные линии</h2>
    <p>Расширились настолько, что имеющихся телефонных линий уже не хватает? Нуждаетесь в дополнительных телефонных линиях? Решите эту проблему с помощью «НОВАТЕЛ»! Новые телефонные линии — одно из приоритетных направлений деятельности нашей компании. Мы способны установить дополнительные телефонные линии практически в любой части Москвы, а также сохранить их вам в случае переезда.</p>
    <h2>Телефонные номера</h2>
    <p>До вас трудно дозвониться? Нужны дополнительные телефонные номера? Обратитесь в «НОВАТЕЛ»! Телефонные номера, а именно: красивые телефонные номера, виртуальные телефонные номера, многоканальные телефонные номера и вообще любые телефонные номера, какими они только могут быть, подпадают в компетенцию нашей деятельности.</p>'''),
 "services/teleconference.html": dict(
   crumb="Телеконференции", title="Телеконференции",
   lead="Телеконференция (аудиоконференция) — это возможность одновременного удалённого общения какого-то числа людей (от 2 до 60, например), находящихся в различных частях города, страны или мира.",
   desc="Телеконференции (аудиоконференции) от НОВАТЕЛ — одновременное удалённое общение от 2 до 60 человек на московских, российских и международных номерах.",
   prose='''    <h2>Зачем это нужно</h2>
    <p>Услуга решает проблему ограниченного количества телефонных линий. Вместо покупки дополнительных линий с ежемесячной платой ради конференций, которые проводятся 2-3 раза в месяц, клиент может использовать услугу телеконференции.</p>
    <h2>На каких номерах</h2>
    <ul class="bullets">
      <li>Московские номера кодов (495), (499)</li>
      <li>Российские номера кода (800)</li>
      <li>Международные номера кода (800)</li>
    </ul>
    <h2>Основные применения</h2>
    <ul class="bullets">
      <li>Удалённая координация сотрудников в различных регионах</li>
      <li>Проведение экспресс-семинаров и тренингов</li>
      <li>Многосторонние переговоры</li>
    </ul>
    <h2>Стоимость</h2>
    <p>Жёсткого прайс-листа на данную услугу нет — тарифы определяются индивидуально в зависимости от потребностей клиента.</p>'''),
 "services/hosting.html": dict(
   crumb="Хостинг", title="Хостинг",
   lead="Круглосуточный бесперебойный доступ к веб-сайту по высокоскоростным каналам связи.",
   desc="Хостинг от НОВАТЕЛ как оператора связи: круглосуточный доступ по высокоскоростным каналам, ориентация на 1С-Битрикс, высокая скорость открытия сайтов.",
   prose='''    <h2>Что это такое</h2>
    <p>Хостинг (от англ. hosting) — в большинстве случаев под этим подразумевается услуга по размещению веб-сайта на сервере хостинг-провайдера или оператора связи, при которой к веб-сайту обеспечивается круглосуточный бесперебойный доступ по высокоскоростным каналам связи.</p>
    <h2>Наша история с хостингом</h2>
    <p>Компания начала оказывать услуги хостинга в 2000 году через своё веб-подразделение, позже преобразованное в самостоятельную веб-студию «Силуэт». Изначально хостинг был доступен только клиентам этой студии, со временем мы начали выборочно обслуживать и сторонних заказчиков, хотя в силу специфики работы компании хостинг по-прежнему ограничен определёнными категориями клиентов.</p>
    <h2>Технический фокус</h2>
    <p>Наш хостинг в первую очередь ориентирован на сайты, использующие CMS «1С-Битрикс», поскольку наша веб-студия работает именно с этой платформой. Другие CMS также могут функционировать на наших серверах, но 1С-Битрикс представляет собой основную ориентацию.</p>
    <h2>В чём преимущество</h2>
    <p>Мы обеспечиваем более высокую скорость открытия сайтов и их доступность по сравнению с большинством хостинг-провайдеров. Причина в том, что мы являемся оператором связи с избыточной пропускной способностью, а не выделенным хостинг-провайдером, зависящим исключительно от доходов с хостинга.</p>
    <h2>Кому доступен хостинг</h2>
    <ul class="bullets">
      <li>Клиентам веб-студии «Силуэт»</li>
      <li>Партнёрским веб-студиям</li>
      <li>Действующим клиентам «НОВАТЕЛ»</li>
      <li>Тем, кого порекомендовали перечисленные выше группы</li>
    </ul>
    <p class="note">Хостинг на базе Windows не предоставляется.</p>'''),
 "services/it-outsourcing.html": dict(
   crumb="ИТ-аутсорсинг", title="ИТ-аутсорсинг",
   lead="Обеспечение бесперебойной работы офисов по принципу «ВСЁ ВКЛЮЧЕНО!».",
   desc="ИТ-аутсорсинг от компании «Стабилити Системс» (группа НОВАТЕЛ): обеспечение бесперебойной работы офисов по принципу «ВСЁ ВКЛЮЧЕНО!».",
   prose='''    <h2>Как появилась услуга</h2>
    <p>Системная интеграция и ИТ-аутсорсинг не являются профильными бизнесами «НОВАТЕЛ», поэтому в 2003 году была создана самостоятельная компания «Стабилити Системс».</p>
    <p>Основной задачей «Стабилити Системс» было и остаётся оказание услуг другим организациям и предпринимателям по обеспечению бесперебойной работы их офисов.</p>
    <h2>Почему вышли на рынок</h2>
    <p>Постоянно сталкиваясь с низким профессиональным уровнем тех, кто обслуживает клиентов «НОВАТЕЛ», мы решили вывести «Стабилити Системс» на публичный рынок и начать оказывать услуги всем желающим.</p>
    <h2>Принцип «ВСЁ ВКЛЮЧЕНО!»</h2>
    <p>Выходя на розничный рынок, мы приняли решение, что будем работать по принципу: «ВСЁ ВКЛЮЧЕНО!»</p>
    <ul class="bullets">
      <li>Полная техническая поддержка офисов без ограничений по выездам.</li>
      <li>Бесплатное размещение веб-сайтов и электронной почты на серверах компании.</li>
      <li>Минимальная поддержка веб-ресурсов с минимальной стоимостью 7500 рублей ежемесячно.</li>
    </ul>'''),
}


# ============================================================
#  СБОРКА 8-800 (промо в верхний уровень)
# ============================================================
EIGHT_PROSE = open(os.path.join(BASE, "_8800_prose.html"), encoding="utf-8").read() if os.path.exists(os.path.join(BASE, "_8800_prose.html")) else None


def build():
    # Верхнеуровневые страницы
    render("index.html", "", "index.html",
           "НОВАТЕЛ — стабильная альтернатива · телекоммуникационная компания",
           "НОВАТЕЛ — телекоммуникационная компания. 29 лет помогаем клиентам. Номера 8-800, IP-телефония, виртуальные и многоканальные номера, телефонизация офисов, междугородная и международная связь.",
           home_body())
    render("vozmozhnosti.html", "", "vozmozhnosti.html",
           "Возможности — НОВАТЕЛ",
           "Услуги НОВАТЕЛ: номер 8-800, IP-телефония, виртуальные и многоканальные номера, телефонизация офисов, междугородная и международная связь, телеконференции, хостинг, ИТ-аутсорсинг.",
           vozmozhnosti_body())
    render("tarify.html", "", "tarify.html",
           "Тарифы — НОВАТЕЛ",
           "Тарифы НОВАТЕЛ: номера 8-800, многоканальный телефон, хостинг. Прозрачные условия, индивидуальный расчёт под объём звонков.",
           tarify_body())
    render("voprosy.html", "", "voprosy.html",
           "Вопросы и ответы — НОВАТЕЛ",
           "Частые вопросы о номерах 8-800, IP-телефонии, виртуальных номерах и услугах НОВАТЕЛ. Новичкам, бывалым и сомневающимся.",
           voprosy_body())
    render("kontakty.html", "", "kontakty.html",
           "Контакты — НОВАТЕЛ",
           "Контакты НОВАТЕЛ: 8 (495) 775-12-87, 8 (800) 775-12-87, info@novatel.ru, Москва, ул. Староалексеевская, д. 5, оф. 363. Оставьте заявку онлайн.",
           kontakty_body())
    # Детальные страницы услуг
    for fname, d in SERVICE_PAGES.items():
        render(fname, "../", "vozmozhnosti.html",
               f"{d['crumb']} — НОВАТЕЛ", d["desc"],
               service_page("../", d["crumb"], "Услуга", d["title"], d["lead"], d["prose"]))
    # 8-800 (верхний уровень) — тело берём из _8800_prose.html
    if EIGHT_PROSE:
        render("8800.html", "", "8800.html",
               "Номер 8-800 — НОВАТЕЛ",
               "Телефонный номер 8-800 — возможность стать ближе к клиентам, которые могут позвонить вам бесплатно. Подключение и обслуживание 800-х номеров — одна из специализаций НОВАТЕЛ.",
               service_page("", "Номер 8-800", "Услуга",
                            "Номер 8&nbsp;800 / Телефон 8&nbsp;800",
                            "Возможность стать ближе к своим клиентам и партнёрам по бизнесу, которые могут позвонить вам бесплатно.",
                            EIGHT_PROSE, cta="buttons"))
    else:
        print("WARN: _8800_prose.html не найден — 8800.html не собран")


if __name__ == "__main__":
    build()
