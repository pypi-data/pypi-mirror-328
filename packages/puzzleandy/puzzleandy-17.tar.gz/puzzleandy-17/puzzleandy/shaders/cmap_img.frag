#version 330

vec2 fragCoord = gl_FragCoord.xy;
uniform sampler2D iChannel0;
uniform sampler2D iChannel1;
uniform vec3 iResolution;

out vec4 fragColor;

void main()
{
	vec2 uv = fragCoord/iResolution.xy;
	float Y = texture(iChannel0,uv).r;
	fragColor = texture(iChannel1,vec2(Y,0.5));
}