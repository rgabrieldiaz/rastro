"""
Cliente Python para OpenARG MCP Server.
Permite invocar las herramientas de datos públicos oficiales de Argentina
directamente desde scripts, agentes de IA (LangGraph, CrewAI) o dashboards (Streamlit).
"""

import os
import json
import ssl
import urllib.request
from typing import Any, Dict, List, Optional
from pathlib import Path

# Cargar variables de entorno desde .env si existe
env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

OPENARG_API_KEY = os.getenv("OPENARG_API_KEY", "oarg_sk_-JNt3Q9bMxIaFSlzxZn-KsiVFWXKEePolIbHZOUHXrs")
OPENARG_MCP_URL = os.getenv("OPENARG_MCP_URL", "https://mcp.openarg.org/mcp")


class OpenArgClient:
    def __init__(self, api_key: Optional[str] = None, url: Optional[str] = None):
        self.api_key = api_key or OPENARG_API_KEY
        self.url = url or OPENARG_MCP_URL
        self.ctx = ssl._create_unverified_context()
        self._req_id = 0

    def _call_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        self._req_id += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self._req_id,
            "method": "tools/call",
            "params": {
                "name": name,
                "arguments": arguments
            }
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        with urllib.request.urlopen(req, context=self.ctx) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            if "error" in raw:
                raise RuntimeError(f"OpenARG error: {raw['error']}")
            
            result = raw.get("result", {})
            content = result.get("content", [])
            texts = [c.get("text", "") for c in content if c.get("type") == "text"]
            return "\n".join(texts)

    def listar_fuentes(self) -> str:
        """Lista los portales de datos abiertos que cubre OpenArg y cuántos datasets tiene cada uno."""
        return self._call_tool("listar_fuentes", {})

    def buscar_datasets(self, texto: str, portal: Optional[str] = None, limite: int = 10) -> str:
        """Busca en el catálogo de OpenArg (+30.000 datasets oficiales)."""
        args: Dict[str, Any] = {"texto": texto, "limite": limite}
        if portal:
            args["portal"] = portal
        return self._call_tool("buscar_datasets", args)

    def describir_tabla(self, tabla: str) -> str:
        """Muestra columnas, cantidad de filas, período cubierto, frescura y muestra de una tabla."""
        return self._call_tool("describir_tabla", {"tabla": tabla})

    def obtener_datos(
        self,
        tabla: str,
        columnas: Optional[List[str]] = None,
        filtros: Optional[Dict[str, Any]] = None,
        limite: int = 100,
        desde: Optional[str] = None,
        hasta: Optional[str] = None,
    ) -> str:
        """Trae filas filtradas de una tabla de OpenArg."""
        args: Dict[str, Any] = {"tabla": tabla, "limite": limite}
        if columnas:
            args["columnas"] = columnas
        if filtros:
            args["filtros"] = filtros
        if desde:
            args["desde"] = desde
        if hasta:
            args["hasta"] = hasta
        return self._call_tool("obtener_datos", args)

    def agregar_datos(
        self,
        tabla: str,
        operacion: str,
        columna_valor: Optional[str] = None,
        columnas_agrupacion: Optional[List[str]] = None,
        orden: Optional[str] = None,
        limite: int = 20,
    ) -> str:
        """Calcula totales, promedios, conteos, mínimos, máximos o rankings agrupados."""
        args: Dict[str, Any] = {
            "tabla": tabla,
            "operacion": operacion,
            "limite": limite
        }
        if columna_valor:
            args["columna_valor"] = columna_valor
        if columnas_agrupacion:
            args["columnas_agrupacion"] = columnas_agrupacion
        if orden:
            args["orden"] = orden
        return self._call_tool("agregar_datos", args)

    def consultar_datos_publicos(self, pregunta: str) -> str:
        """Modo respuestas: responde una pregunta en lenguaje natural citando fuentes oficiales."""
        return self._call_tool("consultar_datos_publicos", {"pregunta": pregunta})


# Instancia por defecto para importar directamente
client = OpenArgClient()

if __name__ == "__main__":
    print("Probando conexión con OpenARG MCP...")
    fuentes = client.listar_fuentes()
    print("Primeras líneas de fuentes:")
    print("\n".join(fuentes.splitlines()[:6]))
