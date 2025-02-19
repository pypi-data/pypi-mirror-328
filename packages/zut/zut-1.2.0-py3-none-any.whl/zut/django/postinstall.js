import fs from 'fs';
import path from 'path';
import { globSync} from 'glob';
import zlib from 'zlib';
import { Readable } from 'stream';
import { finished } from 'stream/promises';
import { ProxyAgent, setGlobalDispatcher } from 'undici';

async function main() {
    const static_dir = path.join(import.meta.dirname, 'static', 'lib');
    const sources_dir = path.join(import.meta.dirname, 'sources', 'lib');
    const base = getNodeModulesDir();

    configureProxy();
    
    copy('bootstrap/LICENSE', static_dir, {base});
    copy('bootstrap/dist/css/bootstrap.min.css', static_dir, {base});
    copy('bootstrap/dist/css/bootstrap.min.css.map', static_dir, {base});
    copy('bootstrap/dist/js/bootstrap.bundle.min.js', static_dir, {base});
    copy('bootstrap/dist/js/bootstrap.bundle.min.js.map', static_dir, {base});

    copy('bootstrap-icons/LICENSE', static_dir, {base});
    copy('bootstrap-icons/font/bootstrap-icons.min.css', static_dir, {base});
    copy('bootstrap-icons/font/fonts/bootstrap-icons.woff', static_dir, {base});
    copy('bootstrap-icons/font/fonts/bootstrap-icons.woff2', static_dir, {base});

    copy('jquery/LICENSE.txt', static_dir, {base});
    copy('jquery/dist/jquery.min.js', static_dir, {base});

    copy('jquery.dirty/LICENSE', static_dir, {base});
    copy('jquery.dirty/dist/jquery.dirty.js', static_dir, {base});

    copy('bootstrap-table/LICENSE', static_dir, {base});
    copy('bootstrap-table/dist/bootstrap-table.min.css', static_dir, {base});
    copy('bootstrap-table/dist/bootstrap-table.min.js', static_dir, {base});
    copy('bootstrap-table/dist/locale/*.min.js', static_dir, {base});

    copy('select2/LICENSE.md', static_dir, {base});
    copy('select2/dist/css/select2.min.css', static_dir, {base});
    copy('select2/dist/js/select2.min.js', static_dir, {base});
    copy('select2/dist/js/i18n/*.js', static_dir, {base});

    copy('select2-bootstrap-5-theme/LICENSE', static_dir, {base});
    copy('select2-bootstrap-5-theme/dist/select2-bootstrap-5-theme.min.css', static_dir, {base});

    // world_countries_lists - See https://stefangabos.github.io/world_countries/
    copy(`world_countries_lists/data/countries/*/countries.json`, sources_dir, {base});
    copy(`world_countries_lists/data/flags/16x16/*.png`, static_dir, {base});

    // db-ip
    await downloadDbIpCountries(`https://db-ip.com/db/download/ip-to-country-lite`, `${sources_dir}/db-ip/GeoLite2-Country.mmdb`);
}

export function configureProxy() {
    if (process.env.HTTP_PROXY) {    
        setGlobalDispatcher(new ProxyAgent(process.env.HTTP_PROXY, {
            requestTls: { // NOTE: `export NODE_TLS_REJECT_UNAUTHORIZED=0` might be required (this option does not seem to be taken into account with Node v20.18.3 - ROADMAP)
                rejectUnauthorized: false,
            }
        }));
    }    
}

/**
 * See: https://db-ip.com/db/download/ip-to-country-lite
 */
export async function downloadDbIpCountries(src, dst) {
    // Determine URL
    let res = await fetch(src);
    const html = await res.text();
    const m = html.match(/href=['"](.+\/dbip\-country\-lite\-.+\.mmdb\.gz)['"]/);
    if (! m) {
        console.error("Cannot find mmdb.gz link");
        return;
    }
    const url = m[1];

    // Check if we need to redownload
    const dstOrigin = `${dst}-origin.txt`;
    if (fs.existsSync(dst) && fs.existsSync(dstOrigin)) {
        const prevUrl = fs.readFileSync(dstOrigin, {encoding:'utf-8'});
        if (prevUrl == url) {
            return;
        }
    }

    // Download and unzip URL
    await download(url, dst, {gunzip: true});
    fs.writeFileSync(dstOrigin, url, {encoding:'utf-8'});
}

export function copy(pattern, target, {base} = {}) {
    if (base === undefined) {
        base = process.cwd();
    }

    const files = globSync(pattern, {cwd: base});
    
    if (files.length == 0) {
        console.error(`[copy] ${pattern}: no file`);
        return;
    }
    
    console.log(`[copy] ${pattern}: ${files.length} file${files.length > 1 ? 's' : ''} ...`);
    
    for (const file of files) {
        const src = path.join(base, file);
        const dst = path.join(target, file);
        fs.mkdirSync(path.dirname(dst), {recursive: true});
        fs.copyFileSync(src, dst);
    }
}

export async function download(url, dst, {gunzip} = {}) {
    console.log(`[download] ${url}`);
    fs.mkdirSync(path.dirname(dst), {recursive: true});
    
    const res = await fetch(url);
    
    let stream = Readable.fromWeb(res.body);
    if (gunzip) {
        stream = stream.pipe(zlib.createGunzip());
    }
    await finished(stream
        .pipe(fs.createWriteStream(dst, { flags: 'w' }))
    );
}

let _nodeModulesDir = null;

export function getNodeModulesDir() {
    if (! _nodeModulesDir) {
        let currentDir = import.meta.dirname;
        let nextDir = null;
        while (true) {
            let possibleDir = path.join(currentDir, 'node_modules');
            if (fs.existsSync(possibleDir)) {
                return possibleDir;
            }

            nextDir = path.dirname(currentDir);
            if (nextDir == currentDir) {
                break;
            }
            currentDir = nextDir;
        }
    }
    return _nodeModulesDir;
}

main().then()
